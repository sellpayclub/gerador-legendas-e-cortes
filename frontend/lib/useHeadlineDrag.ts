"use client";

import { useRef, type PointerEvent } from "react";

/** Headline coordinates match FFmpeg: X uses available travel, Y is its center. */
export function useHeadlineDrag(
  x: number,
  y: number,
  widthPct: number,
  onChange?: (position: { x: number; y: number }) => void,
) {
  const drag = useRef<{ pointerId: number; startX: number; startY: number; x: number; y: number; travel: number; height: number } | null>(null);
  const clamp = (value: number) => Math.max(0, Math.min(1, value));
  const finish = (event: PointerEvent<HTMLDivElement>) => {
    if (drag.current?.pointerId !== event.pointerId) return;
    drag.current = null;
    if (event.currentTarget.hasPointerCapture(event.pointerId)) event.currentTarget.releasePointerCapture(event.pointerId);
  };
  return {
    onPointerDown(event: PointerEvent<HTMLDivElement>) {
      if (!onChange || event.button !== 0) return;
      const frame = event.currentTarget.parentElement?.getBoundingClientRect();
      if (!frame || frame.height <= 0) return;
      event.preventDefault();
      event.stopPropagation();
      drag.current = { pointerId: event.pointerId, startX: event.clientX, startY: event.clientY,
        x, y, travel: frame.width * (1 - widthPct), height: frame.height };
      event.currentTarget.setPointerCapture(event.pointerId);
    },
    onPointerMove(event: PointerEvent<HTMLDivElement>) {
      const state = drag.current;
      if (!state || state.pointerId !== event.pointerId || !onChange) return;
      event.preventDefault();
      event.stopPropagation();
      onChange({ x: state.travel > 0 ? clamp(state.x + (event.clientX - state.startX) / state.travel) : state.x,
        y: clamp(state.y + (event.clientY - state.startY) / state.height) });
    },
    onPointerUp: finish,
    onPointerCancel: finish,
    onLostPointerCapture() { drag.current = null; },
  };
}
