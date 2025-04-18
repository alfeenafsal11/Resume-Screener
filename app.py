import gradio as gr
from Resume_Screening.parser import extract_text
from Resume_Screening.preprocessor import preprocess_text
from Resume_Screening.scorer import resume_check

def process_files(jd_file, resume_file, threshold):
    if jd_file is None or resume_file is None:
        return "❌ Error: Please upload both Job Description and Resume files."

    jd_text = extract_text(jd_file)
    keywords = preprocess_text(jd_text)
    match_result, score = resume_check(resume_file, keywords, threshold)

    result_text = "✅ Resume matches the job description!" if match_result else "❌ Resume does not match the job description."
    return f"{result_text}\n\nMatch Score: {score * 100:.2f}%"

with gr.Blocks() as demo:
    gr.Markdown("# 🧠 Resume Screening App")
    gr.Markdown("Upload a Job Description and a Resume PDF. The app will compare them and return the match score based on extracted keywords.")

    jd_input = gr.File(label="Upload Job Description PDF")
    resume_input = gr.File(label="Upload Resume PDF")
    threshold_input = gr.Slider(minimum=0, maximum=100, value=60, step=1, label="Match Threshold (%)")
    output = gr.Textbox(label="Match Result")

    btn = gr.Button("Match Resume")
    btn.click(fn=process_files, inputs=[jd_input, resume_input, threshold_input], outputs=output)

demo.launch(share=True)
