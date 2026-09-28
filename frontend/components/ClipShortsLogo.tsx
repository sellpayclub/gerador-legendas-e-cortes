import Link from "next/link";

type Props = {
  size?: "sm" | "md" | "lg";
  showTagline?: boolean;
  href?: string;
  className?: string;
};

const heights = { sm: 32, md: 44, lg: 72 };

const logoUrl = "/brand/logo-clipshorts-white.png";

export default function ClipShortsLogo({
  size = "md",
  showTagline = false,
  href,
  className = "",
}: Props) {
  const inner = (
    <div className={`flex flex-col items-center gap-2 ${className}`}>
      <img
        src={logoUrl}
        alt="ClipShorts"
        width={1645}
        height={397}
        className="w-auto object-contain"
        style={{ height: heights[size] }}
      />
      {showTagline && <span className="text-xs uppercase tracking-widest text-muted">Gerador de Legendas</span>}
    </div>
  );

  return href ? (
    <Link href={href} className="inline-block transition opacity-90 hover:opacity-100">{inner}</Link>
  ) : inner;
}
