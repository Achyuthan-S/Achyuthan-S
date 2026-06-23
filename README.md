# Achyuthan Sivasankar

I work on one problem: **how sparse neural systems learn to route computation — and when routing actually helps.**

Currently a research assistant in **Prof. Anna Choromanska's lab at NYU**, working on self-supervised world models for autonomous driving with LiDAR.

---

**What I'm building**
-  **AD-LiST-JEPA** — spatiotemporal JEPA world model for autonomous driving; predicts future BEV LiDAR embeddings without labels or contrastive pairs
-  **KAN-Multi** — routing layer that selects among 6 function bases with zero supervision; +6.8% over MLP on CIFAR-100
-  **MoE-Bench** — open diagnostic toolkit for expert collapse & routing entropy in sparse MoE LLMs (OLMoE, JetMoE, Qwen)

**What I care about**
Self-supervised learning · Sparse MoE architectures · Neural routing · World models · LiDAR perception

**Stack**
Python · PyTorch · C/C++ · Go · HuggingFace · Docker · FastAPI · AWS

---

---

**Notable Open source contributions**


<table>
  <tr>
    <td width="28"><img src="https://github.com/vllm-project.png" width="22" alt="vLLM" /></td>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/44795"><strong>vllm-project/vllm</strong> #44795</a><br/>
      Fix nightly Docker <code>ImportError: AnthropicOutputConfig</code>
    </td>
    <td align="right" width="90">
      <a href="https://github.com/vllm-project/vllm/pull/44795">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" />
      </a>
    </td>
  </tr>
  <tr>
    <td><img src="https://github.com/NVIDIA-NeMo.png" width="22" alt="NeMo" /></td>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2601"><strong>NVIDIA-NeMo/Automodel</strong> #2601</a><br/>
      Re-tie <code>lm_head</code> to active <code>embed_tokens</code> on Gemma4 MoE path
    </td>
    <td align="right">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2601">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" />
      </a>
    </td>
  </tr>
  <tr>
    <td><img src="https://github.com/NVIDIA-NeMo.png" width="22" alt="NeMo" /></td>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2709"><strong>NVIDIA-NeMo/Automodel</strong> #2709</a><br/>
      Cherry-pick #2601 into <code>r0.5.0</code>
    </td>
    <td align="right">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2709">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" />
      </a>
    </td>
  </tr>
</table>

---

📫 [achyuthan.sivasankar@gmail.com](mailto:achyuthan.sivasankar@gmail.com) · [LinkedIn](https://linkedin.com/in/achyuthan-s) · [Portfolio](https://achyuthan-s.web.app)
