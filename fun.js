
async function problemSolving() {
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
    const prompt = "";
    const imageParts = [
        fileToGenerativePart("prob.jpg", "image/jpeg"),
    ];
    const result = await model.generateContent([prompt, ...imageParts]);
    const response = await result.response;
    const text = response.text();
    console.log(text);
    return text;
  }
  
  async function textQuery(query) {
    const model = genAI.getGenerativeModel({ model: "gemini-pro"});
    const result = await model.generateContent(query);
    const response = await result.response;
    const text = response.text();
    return text;
  }
  
  async function syllabusGen(std, sub) {
    const model = genAI.getGenerativeModel({ model: "gemini-pro"});
    const prompt = `Generate the Syllabus of ${std} for the subject ${sub} based on current National Educational Policy and always keep in mind the class of a student.Only generate the syllabus according the class age.`;
    const result = await model.generateContent(prompt);
    const response = await result.response;
    const text = response.text();
    return text;
  }