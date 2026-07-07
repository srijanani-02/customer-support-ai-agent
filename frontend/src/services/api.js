import axios from "axios";

const api = axios.create({
    baseURL: "https://customer-support-ai-agent-oz0j.onrender.com",
    headers: {
        "Content-Type": "application/json",
    },
});

export default api;