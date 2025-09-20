from faster_whisper import WhisperModel
import torch

def transcribe_to_txt(input_file, output_file, model_size="small", debug=True):
    if torch.cuda.is_available():
        device = "cuda"
        compute_type = "float16"
    else:
        device = "cpu"
        compute_type = "int8" 

    print(f"[INFO] Process model '{model_size}' on device={device}, compute_type={compute_type} ...")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)

    print(f"[INFO] start Transcript: {input_file}")
    segments, info = model.transcribe(input_file, beam_size=5)

    text = []
    for seg in segments:
        line = f"[{seg.start:.2f} → {seg.end:.2f}] {seg.text}"
        text.append(line)
        if debug:
            print(line) 
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(text))

    print(f"[INFO] transcript done! saved {output_file}")

if __name__ == "__main__":
    #change "audio.mp3" and "output.txt" to your desired input and output files
    transcribe_to_txt("audio.mp3", "output.txt", model_size="base", debug=True)
