import pt from "./locales/pt";
import en from "./locales/en";
import es from "./locales/es";
import { extraCopy } from "./extra";

export type CopyLocale = "pt" | "en" | "es";
export const LOCALE_STORAGE_KEY = "clipshorts_locale";
export const copyCatalog: Record<string, { en: string; es: string }> = {};
function collect(p: any, e: any, s: any) {
  for (const key of Object.keys(p)) {
    if (typeof p[key] === "string") copyCatalog[p[key]] = { en: e[key], es: s[key] };
    else collect(p[key], e[key], s[key]);
  }
}
collect(pt, en, es);
for (const [source, english, spanish] of extraCopy) {
  if (!source || !english || !spanish) throw new Error(`Incomplete translation: ${source}`);
  copyCatalog[source] = { en: english, es: spanish };
}

export function readLocale(): CopyLocale {
  if (typeof window === "undefined") return "pt";
  try {
    const saved = window.localStorage.getItem(LOCALE_STORAGE_KEY);
    if (saved === "en" || saved === "es" || saved === "pt") return saved;
  } catch { /* Private browsing may block storage. */ }
  const lang = window.navigator.language.slice(0, 2);
  return lang === "en" || lang === "es" ? lang : "pt";
}

let browserLocale: CopyLocale | undefined;
export function setCopyLocale(locale: CopyLocale) { browserLocale = locale; }
export function currentLocale(): CopyLocale {
  return typeof window === "undefined" ? "pt" : browserLocale ?? readLocale();
}
export function intlLocale(): string {
  return { pt: "pt-BR", en: "en-US", es: "es-ES" }[currentLocale()];
}

/** Translate application-owned copy only; never pass transcript/user content. */
export function copy(source: string, params?: Record<string, string | number>, locale = currentLocale()): string {
  const normalized = source.replace(/\s+/g, " ").trim();
  const translated = locale === "pt" ? normalized : copyCatalog[normalized]?.[locale] ?? normalized;
  const result = translated.replace(/\{(\w+)\}/g, (token, name) => params?.[name] === undefined ? token : String(params[name]));
  return (source.startsWith(" ") ? " " : "") + result + (source.endsWith(" ") ? " " : "");
}
