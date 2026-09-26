"use client";
import { useI18n as useLocaleSubscription } from "@/lib/i18n/context";

import { copy } from "@/lib/i18n/copy";


import { useEffect, useState } from "react";
import { createClient } from "@/lib/supabase/client";

/**
 * Private hand-off used by the native ViralClips shell. The session travels in
 * the URL fragment, which browsers do not send to the server, and is replaced
 * immediately after Supabase has persisted it.
 */
export default function MobileSessionPage() {
  useLocaleSubscription();
  const [message, setMessage] = useState(copy("Preparando seu editor..."));

  useEffect(() => {
    const bootstrap = async () => {
      const values = new URLSearchParams(window.location.hash.slice(1));
      const accessToken = values.get("access_token");
      const refreshToken = values.get("refresh_token");
      if (!accessToken || !refreshToken) {
        setMessage(copy("Não foi possível iniciar a sessão do aplicativo."));
        return;
      }
      try {
        const supabase = createClient();
        const { data, error } = await supabase.auth.setSession({
          access_token: accessToken,
          refresh_token: refreshToken,
        });
        if (error || !data.session) throw error || new Error(copy("Sessão ausente"));
        const response = await fetch("/api/mobile/session", {
          method: "POST",
          headers: { Authorization: `Bearer ${data.session.access_token}` },
        });
        if (!response.ok) throw new Error(await response.text());
        window.location.replace("/");
      } catch {
        setMessage(copy("Não foi possível conectar ao ViralClips. Tente novamente."));
      }
    };
    void bootstrap();
  }, []);

  return (
    <main className="flex min-h-[65vh] items-center justify-center px-6 text-center">
      <p className="text-sm text-zinc-300">{message}</p>
    </main>
  );
}
