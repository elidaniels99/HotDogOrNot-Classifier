# HotDogOrNot-Classifier
Hot Dog Detection Streamlit App: Silicon Valley-Inspired

Welcome to the "Hot Dog Detection" Streamlit application, inspired by the popular HBO television series, Silicon Valley. This prototype app enables users to upload an image, where our advanced model will determine the presence of a hot dog. To achieve this, we undertook several critical steps in model development.

**Data Preprocessing** : To ensure compatibility with sequential neural networks, we resized all images in the dataset to a uniform size. Additionally, we converted these images into numpy arrays and normalized them, scaling pixel values from the traditional 0 to 255 RGB range to a more suitable 0 to 1 range, aligning with neural network requirements.

**Model Architecture**s: We rigorously tested several model architectures, including VGG16, ResNet, and Xception, to determine the most effective one for our task. To prevent overfitting, Dropout layers were strategically added after each block of the neural network.

**Loss Function**: Given the binary nature of our problem (hotdog or not-hotdog), we employed BinaryCrossentropy() as the loss function. This choice allows our model to effectively learn and make binary classifications.

**Network Depth**: We opted for a deeper neural network structure, as it is well-suited to handle the intricacies of this problem. The incorporation of AveragePooling2D() as the initial layer was particularly beneficial, as it contributed to better results during the training phase.

The hallmark of this application is its seamless integration with Streamlit, guaranteeing an intuitive and sophisticated user experience, prioritizing user engagement right from the project's inception.

Our overarching objective is to demonstrate the substantial enhancements achieved by our model compared to the baseline, offering valuable insights into the efficacy of techniques such as image resizing, normalization, and advanced model architectures. We will persistently archive the most proficient model to a file and seamlessly integrate it into our Streamlit application for users to experience firsthand.
