from __future__ import annotations

import argparse
import os
import time

import cv2
from ultralytics import YOLO


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run YOLO11n human detection from a camera.")
    parser.add_argument("--model", required=True, help="Path to .pt or .onnx model.")
    parser.add_argument("--camera", type=int, default=0, help="Camera index.")
    parser.add_argument("--conf", type=float, default=0.25, help="Confidence threshold.")
    parser.add_argument("--imgsz", type=int, default=640, help="Inference image size.")
    parser.add_argument("--device", default="cpu", help="Inference device, default: cpu.")
    parser.add_argument("--no-display", action="store_true", help="Run without opening an OpenCV window.")
    return parser.parse_args()


def display_available(no_display: bool) -> bool:
    if no_display:
        return False
    if os.name == "nt":
        return True
    return bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))


def main() -> int:
    args = parse_args()
    show_window = display_available(args.no_display)
    if not show_window:
        print("Running headless: no display window will be opened. Press Ctrl+C to stop.")

    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index: {args.camera}")

    model = YOLO(args.model)
    frame_count = 0
    start = time.perf_counter()

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                print("Camera frame read failed.")
                break

            result = model.predict(
                source=frame,
                conf=args.conf,
                imgsz=args.imgsz,
                device=args.device,
                verbose=False,
            )[0]
            frame_count += 1

            boxes = result.boxes
            person_count = 0 if boxes is None else len(boxes)
            if frame_count % 30 == 0:
                fps = frame_count / max(time.perf_counter() - start, 1e-9)
                print(f"frames={frame_count} persons={person_count} avg_fps={fps:.2f}")

            if show_window:
                cv2.imshow("Edge Human YOLO11n Pi 5", result.plot())
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        cap.release()
        if show_window:
            cv2.destroyAllWindows()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
