# Model Card: Edge Human YOLO11n Pi 5

## Model Details

- Model name: Edge Human YOLO11n Pi 5
- Base model: YOLO11n
- Task: Human/person object detection
- Hardware target: Raspberry Pi 5, CPU-only, no Hailo required
- Formats: `.pt` and `.onnx`
- Classes: `person`

## Intended Uses

- Research
- Education
- Edge AI testing
- Robotics prototypes
- Raspberry Pi AI benchmarking
- UAV and smart camera experiments

## Out-of-Scope Uses

- Biometric identification
- Face recognition
- Tracking specific people
- Production surveillance without review
- Law enforcement deployment
- Safety-critical deployment
- Commercial deployment without license and dataset review

## Limitations

The model may perform poorly or unpredictably in:

- Low light
- Rain or fog
- Motion blur
- Small distant people
- Heavy occlusion
- Unusual camera angles
- Thermal or IR footage if not trained for that input type
- Scenes that differ significantly from the training distribution

## Ethical Considerations

- Do not use this model for identifying people.
- Do not use this model for unlawful surveillance.
- Respect privacy and local law.
- Use human review in safety-related workflows.
- Test thoroughly before any real-world deployment.

## Dataset Statement

The raw training dataset is not released. The model may have been trained with mixed manually labeled and web-collected images. Licenses and rights for every original training image have not been fully cleared, so users should not assume commercial dataset clearance.

See `docs/DATASET_STATEMENT.md` for more detail.
