### Echo-Sort-Website Repository

Welcome to the **Echo-Sort-Website** repository. This repository contains the code for the website's frontend (React) and backend (Python Flask), which integrate seamlessly with the trained machine learning model.

#### **Project Overview**
The website provides an intuitive interface for users to interact with the Echosort system. It allows users to classify objects by uploading images or searching for existing images, and it displays results alongside insightful statistics.

#### **Website Features**
1. **Image Classification:**
   - Users can upload an image or use a search component to select an image.
   - The system analyzes the image using the trained model and outputs the identified category: Plastic, Paper, or Other.
2. **Statistics Dashboard:**
   - Results are stored in a MongoDB database.
   - Users can view metrics such as model accuracy, total classifications performed, and category distributions.
3. **Scalable Design:** Built with React for the client-side and Python Flask for the server-side, ensuring a responsive and scalable application.

#### **Usage**
1. Clone the repository:
   ```bash
   git clone https://github.com/BenBashi/Echo-Sort-Website.git
   ```
2. Navigate to the repository directory.
3. Follow the setup instructions in the `README` file for installing dependencies and starting the server and client.

---

