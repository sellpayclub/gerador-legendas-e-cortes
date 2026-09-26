export type MobileLocale = "pt" | "en" | "es";

export function getMobileLocale(): MobileLocale {
  const language = Intl.DateTimeFormat().resolvedOptions().locale.toLowerCase();
  if (language.startsWith("es")) return "es";
  if (language.startsWith("en")) return "en";
  return "pt";
}

const messages: Record<string, Record<MobileLocale, string>> = {
  "Não foi possível iniciar o aplicativo.": { pt: "Não foi possível iniciar o aplicativo.", en: "Unable to start the app.", es: "No fue posible iniciar la aplicación." },
  "Preparando o ViralClips...": { pt: "Preparando o ViralClips...", en: "Preparing ViralClips...", es: "Preparando ViralClips..." },
  "Tentar novamente": { pt: "Tentar novamente", en: "Try again", es: "Intentar de nuevo" },
  "Assinatura pendente": { pt: "Assinatura pendente", en: "Subscription pending", es: "Suscripción pendiente" },
  "Conclua a assinatura para salvar o vídeo.": { pt: "Conclua a assinatura para salvar o vídeo.", en: "Complete your subscription to save the video.", es: "Completa la suscripción para guardar el video." },
  "Não foi possível abrir o pagamento": { pt: "Não foi possível abrir o pagamento", en: "Unable to open payment", es: "No fue posible abrir el pago" },
  "Tente novamente em alguns instantes.": { pt: "Tente novamente em alguns instantes.", en: "Please try again in a moment.", es: "Inténtalo de nuevo en unos instantes." },
  "Configuração do aplicativo incompleta.": { pt: "Configuração do aplicativo incompleta.", en: "App configuration is incomplete.", es: "La configuración de la aplicación está incompleta." },
  "A chave do RevenueCat ainda não foi configurada.": { pt: "A chave do RevenueCat ainda não foi configurada.", en: "The RevenueCat key has not been configured yet.", es: "La clave de RevenueCat aún no está configurada." },
  "Use a chave pública Android do RevenueCat, ou habilite a chave Test Store somente no build interno.": { pt: "Use a chave pública Android do RevenueCat, ou habilite a chave Test Store somente no build interno.", en: "Use the RevenueCat Android public key, or enable the Test Store key only in an internal build.", es: "Usa la clave pública de Android de RevenueCat o habilita la clave Test Store solo en una compilación interna." },
  "Não foi possível criar a sessão anônima.": { pt: "Não foi possível criar a sessão anônima.", en: "Unable to create the anonymous session.", es: "No fue posible crear la sesión anónima." },
  "Não foi possível iniciar sua sessão móvel.": { pt: "Não foi possível iniciar sua sessão móvel.", en: "Unable to start your mobile session.", es: "No fue posible iniciar tu sesión móvil." },
};

export function mobileText(text: string, locale = getMobileLocale()): string {
  return messages[text]?.[locale] ?? text;
}
