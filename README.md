# Achyuthan Sivasankar

I work on one problem: **how sparse neural systems learn to route computation — and when routing actually helps.**

Currently a research assistant in **Prof. Anna Choromanska's lab at NYU**, working on self-supervised world models for autonomous driving with LiDAR.

---
### Papers
**Circuit Synchronization Precedes Generalization: A Causal Precursor to Grokking**
<br><sub>Introduces the **Frequency Synchronization Degree (FSD)** — a permutation-tested metric that detects Fourier-circuit formation **500–3,000 steps before grokking**, with causal weight-decay evidence that the memorization→generalization gap is a regularization phenomenon. Transfers to the non-abelian group S₅. Sole author.</sub>
<br><sub>📄 [arXiv:2606.12966](https://arxiv.org/abs/2606.12966)</sub>

**Adaptive Compute in Latent World Models: When Depth Helps, Hurts, or Doesn't Matter**
<br><sub>Pre-registered study of adaptive-depth latent world models across nine DeepMind Control tasks. Maps when extra depth helps rollouts (ρ up to 4.7×), when shallow beats deep (2/9 tasks), and the routability catch-22 created by early-exit supervision.</sub>
<br><sub>📄 [arXiv:2607.10203](https://arxiv.org/abs/2607.10203)</sub>


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
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/49226"><strong>vllm-project/vllm</strong> #49226</a><br/>
      Disable cross-layer KV blocks for per-token-head quant — fixes <code>OffloadingConnector</code> KV-cache corruption
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project">
        <img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/vllm-project/vllm/pull/49226">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA/Megatron-LM/pull/5743"><strong>NVIDIA/Megatron-LM</strong> #5743</a><br/>
      Support HSDP deferred DP-outer gradient reduction in experimental Megatron-FSDP
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA/Megatron-LM/pull/5743">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2998"><strong>NVIDIA-NeMo/Automodel</strong> #2998</a><br/>
      Single <code>tie_word_embeddings</code> guard via per-class <code>TieSupport</code> (BOTH / TIED_ONLY / UNTIED_ONLY) + <code>from_pretrained</code> flip check
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2998">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2896"><strong>NVIDIA-NeMo/Automodel</strong> #2896</a><br/>
      Complete <code>tie_word_embeddings</code> guards for remaining #2512 model families
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2896">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/47379"><strong>vllm-project/vllm</strong> #47379</a><br/>
      Recover raw tail when GPT-OSS Harmony parser ends non-terminal (Responses API)
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project">
        <img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/vllm-project/vllm/pull/47379">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/4601"><strong>NVIDIA-NeMo/Megatron-Bridge</strong> #4601</a><br/>
      Make finetuning batch sampler epoch-aware on checkpoint resume
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/4601">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/47062"><strong>vllm-project/vllm</strong> #47062</a><br/>
      Return raw output when GPT-OSS Harmony parser ends in a non-terminal state
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project">
        <img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/vllm-project/vllm/pull/47062">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2805"><strong>NVIDIA-NeMo/Automodel</strong> #2805</a><br/>
      Reject <code>tie_word_embeddings=True</code> on separate-head model families
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2805">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/deepspeedai/DeepSpeed/pull/8078"><strong>deepspeedai/DeepSpeed</strong> #8078</a><br/>
      Avoid CUDA context initialization during import-time op compatibility checks (fork-safe import)
    </td>
    <td align="center" width="170">
      <a href="https://github.com/deepspeedai">
        <img src="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/assets/deepspeedai-badge.svg" alt="deepspeedai" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/deepspeedai/DeepSpeed/pull/8078">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2732"><strong>NVIDIA-NeMo/Automodel</strong> #2732</a><br/>
      Resolve <code>tie_word_embeddings</code> top-level-first to match HF tying semantics
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2732">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/44795"><strong>vllm-project/vllm</strong> #44795</a><br/>
      Fix nightly Docker <code>ImportError: AnthropicOutputConfig</code>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project">
        <img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/vllm-project/vllm/pull/44795">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2601"><strong>NVIDIA-NeMo/Automodel</strong> #2601</a><br/>
      Re-tie <code>lm_head</code> to active <code>embed_tokens</code> on Gemma4 MoE path
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2601">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2709"><strong>NVIDIA-NeMo/Automodel</strong> #2709</a><br/>
      Cherry-pick #2601 into <code>r0.5.0</code>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA">
        <img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="30" />
      </a>
    </td>
    <td align="right" width="120">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2709">
        <img src="https://img.shields.io/badge/-merged-8957E5?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged" height="30" />
      </a>
    </td>
  </tr>
</table>

---

## Personal Portfolio

<div align="center">
  <a href="https://achyuthan-s.web.app" target="_blank">
    <img src="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/portfolio_preview.jpeg" width="900" alt="Portfolio preview" style="border-radius: 8px; border: 1px solid #30363d;" />
  </a>
  <br/><br/>
  <a href="https://achyuthan-s.github.io" target="_blank"><strong>→ achyuthan-s.web.app</strong></a>
</div>

---

📫 [as21154@nyu.edu](mailto:as21154@nyu.edu) · [achyuthan.sivasankar@gmail.com](mailto:achyuthan.sivasankar@gmail.com) · [LinkedIn](www.linkedin.com/in/achyuthan-sivasankar-b0814b221) · [Portfolio](https://achyuthan-s.github.io)
