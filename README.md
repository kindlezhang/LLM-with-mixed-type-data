# Overview

Large Language Models (LLMs) are increasingly applied to biomedical research involving mixed-type data, such as structured EHRs, unstructured clinical text, and medical imaging (MRI, Echo, PET, CT). These models support integrative analysis by learning from multimodal inputs, enabling novel insights in disease prediction and personalized medicine. Emerging software frameworks combine LLMs with domain-specific tools to facilitate scalable and interpretable biomedical applications.

In the field of AI health﻿, there is a severe scarcity of domain-specific data. Most datasets rely heavily on labels provided by medical professionals, which results in limited data availability. Consequently, training models becomes very challenging. In this context, transfer learning and fine-tuning techniques become critically important.

# Objectives

1. **Multimodal**  
   - Utilize mainstream feature extraction techniques such as ViT, CLIP﻿, MLLM, BILP, and LoRA to extract features from images and text, and perform semantic alignment.
  
2. **Compare**  
   - Compare the advantages and disadvantages of these different methods and identify their suitable application scenarios.

3. **CNN & transformer**  
   - Incorporate CNN technology and explore new methods to integrate convolutional neural networks with attention mechanisms.

# Data Sources

- ** ImageNet
- ** RadImagenet
- ** Biobank 
- ** PhysioNet https://physionet.org/about/database/#overview
               https://physionet.org/content/mimic-cxr/2.1.0/
               TN-Mammo: A Multi-view Mammography Dataset for Breast Density Classification https://physionet.org/content/tn-mammo-breast-density/1.0.0/TNMammo/#files-panel
               RadVLM Instruction Dataset https://physionet.org/content/radvlm-instruction-dataset/1.0.0/
               https://stanfordmlgroup.github.io/competitions/chexpert/

- ** kaggle https://www.kaggle.com/
            https://www.kaggle.com/datasets/programmer3/digital-twin-ehr-imaging-and-iot-data
- ** shaip https://www.shaip.com/
- ** github awesome public datasets

# Steps in the Study

1. Collect and preprocess the data to ensure high quality of both image and text data.

2. Apply various pretrained feature extraction models to obtain multimodal features.

3. Design and optimize strategies for semantic alignment of images and texts.

4. Conduct experiments and comparisons across different feature extraction and fusion methods to evaluate performance.

5. Investigate hybrid model architectures that combine CNN and attention mechanisms.

6. Analyze results and provide practical technical solutions.

# Expected Outcomes

1. Develop a multimodal feature extraction and alignment framework suitable for medical health applications.

2. Clarify strengths and limitations of various techniques and recommend best use cases.

3. Propose innovative models combining CNNs with attention mechanisms to enhance multimodal data processing.

4. Facilitate improved efficiency and accuracy for AI model training in healthcare domains.

# Importance of the Study

This study addresses the critical challenge of data scarcity in medical AI by leveraging advanced transfer learning and multimodal techniques. It aims to significantly enhance AI applications in healthcare, improving diagnostic support and disease prediction, ultimately benefiting patient outcomes and medical efficiency.



