import { StatusBar } from "expo-status-bar";
import { useEffect, useMemo, useRef, useState } from "react";
import { ActivityIndicator, Alert, Pressable, StyleSheet, Text, View } from "react-native";
import { WebView } from "react-native-webview";
import type { Session } from "@supabase/supabase-js";
import { config, missingConfiguration } from "./src/config";
import { configurePurchases, hasProAccess, presentProPaywall } from "./src/revenuecat";
import { getMobileSession, syncEntitlement } from "./src/session";
import { getMobileLocale, mobileText } from "./src/i18n";

export default function App() {
  const locale = getMobileLocale();
  const webRef = useRef<WebView>(null);
  const [session, setSession] = useState<Session | null>(null);
  const [error, setError] = useState<string | null>(() => {
    const initial = missingConfiguration();
    return initial ? mobileText(initial, getMobileLocale()) : null;
  });
  const [loading, setLoading] = useState(!missingConfiguration());

  useEffect(() => {
    if (error) return;
    const start = async () => {
      try {
        const nextSession = await getMobileSession();
        const info = await configurePurchases(nextSession.user.id);
        if (hasProAccess(info)) await syncEntitlement(nextSession.access_token);
        setSession(nextSession);
      } catch (cause) {
        setError(mobileText(cause instanceof Error ? cause.message : "Não foi possível iniciar o aplicativo.", locale));
      } finally {
        setLoading(false);
      }
    };
    void start();
  }, [error]);

  const editorUrl = useMemo(() => {
    if (!session) return "";
    const fragment = new URLSearchParams({ access_token: session.access_token, refresh_token: session.refresh_token });
    return `${config.appUrl}/mobile#${fragment.toString()}`;
  }, [session]);

  const openPaywall = async () => {
    if (!session) return;
    try {
      await presentProPaywall();
      const info = await configurePurchases(session.user.id);
      if (hasProAccess(info) && await syncEntitlement(session.access_token)) {
        webRef.current?.reload();
        return;
      }
      Alert.alert(mobileText("Assinatura pendente", locale), mobileText("Conclua a assinatura para salvar o vídeo.", locale));
    } catch {
      Alert.alert(mobileText("Não foi possível abrir o pagamento", locale), mobileText("Tente novamente em alguns instantes.", locale));
    }
  };

  if (loading || error || !session) {
    return (
      <View style={styles.loading}>
        {loading ? <ActivityIndicator color="#FFD21F" size="large" /> : null}
        <Text style={styles.loadingText}>{error || mobileText("Preparando o ViralClips...", locale)}</Text>
        {error ? <Pressable style={styles.retry} onPress={() => { setError(null); setLoading(true); }}><Text style={styles.retryText}>{mobileText("Tentar novamente", locale)}</Text></Pressable> : null}
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <WebView
        ref={webRef}
        source={{ uri: editorUrl }}
        onMessage={(event) => {
          try {
            if (JSON.parse(event.nativeEvent.data)?.type === "mobile_export_required") void openPaywall();
          } catch { /* Ignore messages not sent by the editor bridge. */ }
        }}
        javaScriptEnabled
        domStorageEnabled
        sharedCookiesEnabled
        thirdPartyCookiesEnabled
      />
      <StatusBar style="light" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: "#05080D" },
  loading: { flex: 1, backgroundColor: "#05080D", alignItems: "center", justifyContent: "center", padding: 24 },
  loadingText: { color: "#F7F7F7", marginTop: 18, textAlign: "center" },
  retry: { marginTop: 20, backgroundColor: "#FFD21F", borderRadius: 10, paddingHorizontal: 18, paddingVertical: 12 },
  retryText: { color: "#111", fontWeight: "700" },
});
