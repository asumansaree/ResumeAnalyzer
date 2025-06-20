def evaluate_job_requirements_percentage(job_advert_text, detected_tags):
    requirements = [
        "Bilgisayar Mühendisliği Lisans derecesi",
        "Bilgisayar Mühendisliği Yüksek Lisans",
        "Makine görüşü",
        "görüntü işleme",
        "Python, C/C++, OpenCV",
        "Tercihen: Yolo, TensorFlow ve Keras, derin öğrenme, Nvidia CUDA",
        "Kendini motive edebilen, ısrarcı, ahlaklı, çalışkan, yeni teknolojilere hızlı uyum sağlayan dinamik bir birey. Çözüm odaklı, girişimci olmalı ve ekip ortamına olumlu katkı sağlamalıdır.",
        "B2/C1 İngilizce"
    ]

    total_requirements = len(requirements)
    fulfilled_requirements = 0
    fulfilled_requirements_list = []

    for i, requirement_text in enumerate(requirements):
        # Check if the requirement text is present in the detected tags
        if any(requirement_text.lower() in tag.lower() for tag in detected_tags):
            fulfilled_requirements += 1
            fulfilled_requirements_list.append(requirement_text)

    percentage_fulfilled = (fulfilled_requirements / total_requirements) * 100
    result = f"{percentage_fulfilled:.2f}%"

    # Print the fulfilled requirements
    if fulfilled_requirements_list:
        print("You only fulfill the following requirement(s):")
        for requirement in fulfilled_requirements_list:
            print("-", requirement)
    else:
        print("No requirements fulfilled.")

    return result

# Example usage:
# Assuming detected_tags is the list of tags obtained from your model
job_advert_path = "ilan1_requirements.txt"
with open(job_advert_path, "r", encoding="utf-8") as job_advert_file:
    job_advert_text = job_advert_file.read()

detected_tags = ["B-DEG", "Makine görüşü", "I-SKILLS", "I-SKILLS"]
print("Candidate is evaluating...")
result_percentage = evaluate_job_requirements_percentage(job_advert_text, detected_tags)
print("Your compliance score is: ", result_percentage)

