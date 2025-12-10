# Project Report: AI Counseling Interface Transformation / 專案報告：AI 諮詢介面轉型

## Abstract / 摘要

**Transforming Raw Data into Future Experiences: The "Future Advisor" Project**
**將原始數據轉化為未來體驗：「未來諮詢師」專案**

This project successfully upgrades a Jupyter Notebook-based prototype ("University Major Counseling Chatbot") into a high-fidelity, production-grade Streamlit application. By extracting the core logic of Google Gemini API integration and refactoring it into a modular architecture, we bridged the gap between data science experiments and end-user products.

本專案成功將基於 Jupyter Notebook 的原型（「大學入學選系諮商師」）升級為高保真、生產級的 Streamlit 應用程式。透過萃取 Google Gemini API 的核心邏輯並重構為模組化架構，我們跨越了數據科學實驗與終端用戶產品之間的鴻溝。

**1. Core Design Language / 核心設計語言**
We adopted a **"Future Data Interface"** aesthetic. Moving away from standard UI, we implemented a custom **Glassmorphism** system using CSS injection. The visual identity features a **Deep Void Black** backdrop (#050510) accented with **Holographic Blue** and **Neon Cyan**, utilizing frosted glass styling (`backdrop-filter`) to convey depth, professionalism, and a technologically advanced atmosphere tailored for Gen Z users.

我們採用了**「未來數據介面」**美學。擺脫標準介面，我們透過 CSS 注入實作了客製化的**玻璃擬態 (Glassmorphism)** 系統。視覺識別以**深淵黑** (#050510) 為底，點綴**全息藍**與**霓虹青**，並運用磨砂玻璃效果 (`backdrop-filter`) 來傳達深度、專業感以及專為 Z 世代用戶量身打造的科技氛圍。

**2. User Experience Enhancement / 使用者體驗強化**
To utilize the latency of LLMs as a feature rather than a bug, we designed a **cinema-grade interaction flow**. Instead of generic spinners, a **"Micro-skeleton"** animation simulates the AI's cognitive process. Responses are delivered via a **Token-by-token Typewriter Effect** with a glowing gradient cursor, mimicking the flow of thought and significantly increasing user retention and immersion.

為了將大型語言模型的延遲轉化為特色而非缺陷，我們設計了**電影級的互動流程**。取捨棄通用的載入轉圈，改用**「微骨架 (Micro-skeleton)」**動畫模擬 AI 的認知過程。回應透過帶有發光漸層游標的**逐字打字機特效**呈現，模仿思維的流動，顯著提升了用戶的留存率與沉浸感。

**3. Business Value / 商業價值**
The transformation elevates a functional tool into a **Brand Asset**. The robust error handling (auto-retries for 503/429 errors) ensures service reliability, while the premium aesthetic establishes immediate trust. This codebase provides a scalable template for deploying high-value AI consultancy services, proving that style and substance can coexist to drive user engagement.

此次轉型將功能性工具提升為**品牌資產**。強大的錯誤處理機制（針對 503/429 錯誤的自動重試）確保了服務可靠性，而優質的美學設計則建立了即時的信任感。此程式碼庫為部署高價值的 AI 顧問服務提供了可擴展的範本，證明了風格與實質可以並存，從而驅動用戶參與。
