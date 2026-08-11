<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/assets/hero-light.svg">
  <img alt="Achyuthan Sivasankar — sparse neural routing, world models, LiDAR at NYU" src="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/assets/hero-dark.svg" width="100%">
</picture>

<div align="center">
  <a href="https://github.com/Achyuthan-S?tab=repositories">
    <img alt="Merged upstream into the LLM stack" src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=3500&pause=1000&color=3FB950&center=true&vCenter=true&width=760&height=42&lines=Merged+upstream+into+the+LLM+stack;vLLM,+NVIDIA,+DeepSpeed,+NeMo;13%2B+PRs+merged+into+frontier+LLM+training+%26+inference">
  </a>
</div>

<div align="center">
  <sub><b>CONTRIBUTES TO &nbsp;·&nbsp; FRONTIER LLM TRAINING &amp; INFERENCE</b></sub>
  <br/><br/>
  <a href="https://github.com/vllm-project"><img src="https://github.com/vllm-project.png?size=160" width="60" height="60" alt="vLLM" /></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/NVIDIA"><img src="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/assets/nvidia-logo.svg" width="60" height="60" alt="NVIDIA" /></a>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/deepspeedai"><img src="https://github.com/deepspeedai.png?size=160" width="60" height="60" alt="DeepSpeed" /></a>
</div>

---

## `$ cat about.md`

Research assistant in **Prof. Anna Choromanska's lab at NYU** (sparse neural routing · self-supervised world models · LiDAR). Alongside the research, I contribute upstream to the **LLM training & inference stack** — vLLM, NVIDIA NeMo / Megatron, DeepSpeed — chasing correctness bugs in quantized KV caches, weight-tying, checkpointing, and build pipelines.

Open to **research internships, PhD positions, and ML-systems / research-engineering roles** in efficient training, sparse MoE, and world models.

---

## `$ git log --merged --upstream`

<div align="center">
  <img src="https://img.shields.io/badge/PRs_MERGED-13%2B-3FB950?style=for-the-badge&labelColor=0D1117" height="30" alt="13+ PRs merged" />
  &nbsp;
  <img src="https://img.shields.io/badge/UPSTREAM_ORGS-4-58A6FF?style=for-the-badge&labelColor=0D1117" height="30" alt="4 upstream orgs" />
  &nbsp;
  <img src="https://img.shields.io/badge/PREPRINTS-2-D29922?style=for-the-badge&labelColor=0D1117" height="30" alt="2 preprints" />
</div>

<br/>

<img src="https://img.shields.io/badge/01-INFERENCE_CORRECTNESS-161B22?style=for-the-badge&labelColor=3FB950" height="28" alt="INFERENCE_CORRECTNESS" />

<sub>Silently wrong or truncated output on live serving paths.</sub>

<table>
  <tr>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/49226"><strong>vllm-project/vllm</strong></a><br/>
      <sub>Disables cross-layer KV blocks under per-token-head quant — stops <code>OffloadingConnector</code> corrupting the KV cache</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project"><img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/vllm-project/vllm/pull/49226"><img src="https://img.shields.io/badge/merged-%2349226-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #49226" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/47379"><strong>vllm-project/vllm</strong></a><br/>
      <sub>Recovers the raw tail when the GPT-OSS Harmony parser ends non-terminal (Responses API)</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project"><img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/vllm-project/vllm/pull/47379"><img src="https://img.shields.io/badge/merged-%2347379-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #47379" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/47062"><strong>vllm-project/vllm</strong></a><br/>
      <sub>Returns raw output instead of dropping it when Harmony parsing ends in a non-terminal state</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project"><img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/vllm-project/vllm/pull/47062"><img src="https://img.shields.io/badge/merged-%2347062-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #47062" height="28" /></a>
    </td>
  </tr>
</table>

<br/>

<img src="https://img.shields.io/badge/02-WEIGHT_TYING-161B22?style=for-the-badge&labelColor=58A6FF" height="28" alt="WEIGHT_TYING" />

<sub>Six PRs closing out <code>tie_word_embeddings</code> across NeMo Automodel, so tied and untied checkpoints load correctly.</sub>

<table>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2998"><strong>NVIDIA-NeMo/Automodel</strong></a><br/>
      <sub>Collapses every guard into one per-class <code>TieSupport</code> (BOTH / TIED_ONLY / UNTIED_ONLY) + a <code>from_pretrained</code> flip check</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2998"><img src="https://img.shields.io/badge/merged-%232998-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #2998" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2896"><strong>NVIDIA-NeMo/Automodel</strong></a><br/>
      <sub>Completes the guards for the remaining #2512 model families</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2896"><img src="https://img.shields.io/badge/merged-%232896-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #2896" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2805"><strong>NVIDIA-NeMo/Automodel</strong></a><br/>
      <sub>Rejects <code>tie_word_embeddings=True</code> on separate-head families instead of silently mis-loading</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2805"><img src="https://img.shields.io/badge/merged-%232805-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #2805" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2732"><strong>NVIDIA-NeMo/Automodel</strong></a><br/>
      <sub>Resolves <code>tie_word_embeddings</code> top-level-first, matching HF tying semantics</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2732"><img src="https://img.shields.io/badge/merged-%232732-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #2732" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2601"><strong>NVIDIA-NeMo/Automodel</strong></a><br/>
      <sub>Re-ties <code>lm_head</code> to the active <code>embed_tokens</code> on the Gemma4 MoE path</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2601"><img src="https://img.shields.io/badge/merged-%232601-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #2601" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2709"><strong>NVIDIA-NeMo/Automodel</strong></a><br/>
      <sub>Cherry-picks #2601 into <code>r0.5.0</code></sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA-NeMo/Automodel/pull/2709"><img src="https://img.shields.io/badge/merged-%232709-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #2709" height="28" /></a>
    </td>
  </tr>
</table>

<br/>

<img src="https://img.shields.io/badge/03-TRAINING_RELIABILITY-161B22?style=for-the-badge&labelColor=D29922" height="28" alt="TRAINING_RELIABILITY" />

<sub>Long runs that resume wrong, imports that deadlock, nightlies that don't ship.</sub>

<table>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA/Megatron-LM/pull/5743"><strong>NVIDIA/Megatron-LM</strong></a><br/>
      <sub>Supports HSDP deferred DP-outer gradient reduction in experimental Megatron-FSDP</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA/Megatron-LM/pull/5743"><img src="https://img.shields.io/badge/merged-%235743-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #5743" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/4601"><strong>NVIDIA-NeMo/Megatron-Bridge</strong></a><br/>
      <sub>Makes the finetuning batch sampler epoch-aware, so checkpoint resume stops replaying the wrong data</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/NVIDIA"><img src="https://img.shields.io/badge/NVIDIA-21262d?style=flat-square&logo=nvidia&logoColor=76B900&labelColor=21262d" alt="NVIDIA" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge/pull/4601"><img src="https://img.shields.io/badge/merged-%234601-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #4601" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/deepspeedai/DeepSpeed/pull/8078"><strong>deepspeedai/DeepSpeed</strong></a><br/>
      <sub>Avoids CUDA context init during import-time op checks — makes <code>import deepspeed</code> fork-safe</sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/deepspeedai"><img src="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/assets/deepspeedai-badge.svg" alt="DeepSpeed" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/deepspeedai/DeepSpeed/pull/8078"><img src="https://img.shields.io/badge/merged-%238078-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #8078" height="28" /></a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="https://github.com/vllm-project/vllm/pull/44795"><strong>vllm-project/vllm</strong></a><br/>
      <sub>Fixes the nightly Docker <code>ImportError: AnthropicOutputConfig</code></sub>
    </td>
    <td align="center" width="150">
      <a href="https://github.com/vllm-project"><img src="https://img.shields.io/badge/vLLM-21262d?style=flat-square&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC%2BaJAAAEVklEQVR4nOyaW3PbRBTH17Iu9kqW5CQOmUlru6EJl%2BFSCJdCn%2FkQvFJguAyfiufCA%2FDCAzwwAwzMpEwhtpNML%2BFiuylJ42BbvkgrRvaguHZWe1YWkTvj31vko939R9rd%2Fzkr0XVd9DgjxD2AaZkLiJu5gLiZC%2FifIYQRIJ7TQPj5p4O%2B3iZYcd962hVF6jhnUUDPRt9UyFe%2FulYfvf1stddbfGwE2AR9t%2BsN%2Fdjy%2FkwmyGqmgzEOuGVWBBCCfrhDvrzlPmieXizobU1NB984EwJ%2B%2BcO9sUVqjfHrl8x28L8%2FfgHlGvpsy7l7ePavRaONcTa4hdgE7B%2BiG1tOqUYN0KT%2BkkpSqVRwOzEIqDfQF7ecn%2B6iYB%2Bf1y1VVZmtnauAh230%2BU3y4x2XAHKQgtFWVY0ZRhdgt4nT5R0iEpKCpNN%2B%2FHaHfH8bmj9d9J7AE8wwqoDe0c2Tnz8BdnaK%2BqR29VPai1uqQkdvKr1cJhmwf%2FlQvZC8fE3Mvgjsz8fu243GxHI4oNlF9yirzSQFg72ADgkyc3jjQ2iHAHbqLF82Qj5jRSBAXnpNXHgZ3mswlTr0%2FUkg96LBcBA%2BDDuNL78L7JXJ7n1o5BLuLmhiMpmEBDMEyLmrovEctGc6zQ766xgaXARPAFBCgzc%2BgPZMp1znCF7zdgD2FjaELUBefnP6h1CpO8BISSCrejedZphQH1BKiZ%2F6GNgcDfgEWNUsDacEAZrrguLk3OtiNvxy9LCFJq0yjbwBskA%2BUKF4%2FTq80THKXDuAzjEBOATIuTdCbMxDyjXoDqAknVXdYVroUTjKKnjjI3jwKNtVaOTAwEEX0CEcAuSlV8WFV7haR8hb%2Fk860OC8zrEDDOErbOH197jiB%2B8PxwQo6FAL5MMnwHsI2Stct%2ByALRCW7BXdlWWZq33u0iKXOyIu2juABhf4358wAryNGbwc%2FXnkpQFA1gBFlEnCFHfhy1GFYwdwizwWyCeMgMFMeAkSWbkPnQC5dNdURUgOOUbI8jpef58Z4xC0B7ZAeYN7%2FRkSUoDnjszng2P2D5HVhzaYz%2FBZIJ%2FwBxxp1kPYrkIngMCTQ07cGxZl%2BZpoBuUJJbAFWtE6pqbALfQoUx0xBSxHnT66%2FQDaDqQKTWMqAV7GvLB55k97BwhSPxyyZrTCTYAIDvnw5XfOvA7fAVKivZKxuSz0KNMK8PIE84XJ67tgC3Qh01FxOpFIhBtABMeskxmz1UP7R9DbeVOwMSIQMMgTHsmYK3WOCVCAnQPQiOage6yK%2BlsVWkRRpX4ICz1KNALkxU3RPLWoJXgOCS7i0ojsU4P0f8na381HjkqDyfOnYGNEJkDx8oQrXDWsQRl0ZgT4M%2BHesQKMN5ReThckSZqm0ygFDJajzd9PoGXNotGG10BpRHxKKV66fuHAdmxQHvnMYpN5js0kEflnl61Wy7IsYHA2mwUeZNCIXsA5M%2BtfbDGZC4ibuYC4mQuIm38DAAD%2F%2F%2B19NjEX7JQMAAAAAElFTkSuQmCC&labelColor=21262d" alt="vLLM" height="28" /></a>
    </td>
    <td align="right" width="150">
      <a href="https://github.com/vllm-project/vllm/pull/44795"><img src="https://img.shields.io/badge/merged-%2344795-8957E5?style=flat-square&labelColor=21262d&logo=data:image/svg%2Bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik01LjQ1IDUuMTU0QTQuMjUgNC4yNSAwIDAgMCA5LjI1IDcuNWgxLjM3OGEyLjI1MSAyLjI1MSAwIDEgMSAwIDEuNUg5LjI1QTUuNzM2IDUuNzM2IDAgMCAxIDUgNy45djMuMTU0YS4yNS4yNSAwIDAgMS0uNDI3LjE3N0wyLjI1NCA5LjQyN2EuMjUuMjUgMCAwIDEgMC0uMzU0bDIuMzE5LTIuMzJhLjI1LjI1IDAgMCAxIC40MjcuMTc3Wm0tLjcwNyAxLjQ0MmEyLjc1IDIuNzUgMCAwIDEgMC0zLjc5Mkw3LjI4MyAxLjA4YS4yNS4yNSAwIDAgMSAuNDI3LjE3N1Y0Ljc1QTQuMjUgNC4yNSAwIDAgMSAxMS43NSA5aDEuMzc4YTIuMjUxIDIuMjUxIDAgMSAwIDAtMS41SDExLjc1QTUuNzM2IDUuNzM2IDAgMCAwIDcuOSA1SDUuNzQzWk0zLjU2IDcuMjVhLjI1LjI1IDAgMCAwLS40MjctLjE3N0wuODE0IDkuMzIzYS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMTkgMi4zMmEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3VjcuMjVaTTYuNSAxMC43NWEuMjUuMjUgMCAwIDAtLjQyNy0uMTc3bC0yLjMyIDIuMzE5YS4yNS4yNSAwIDAgMCAwIC4zNTRsMi4zMiAyLjMxOWEuMjUuMjUgMCAwIDAgLjQyNy0uMTc3di00LjQ4NloiLz48L3N2Zz4=" alt="merged #44795" height="28" /></a>
    </td>
  </tr>
</table>

---

## `$ cat preprints.bib`

**Circuit Synchronization Precedes Generalization: A Causal Precursor to Grokking**
<br><sub>Introduces the **Frequency Synchronization Degree (FSD)** — a permutation-tested metric that detects Fourier-circuit formation **500–3,000 steps before grokking**, with causal weight-decay evidence that the memorization→generalization gap is a regularization phenomenon. Transfers to the non-abelian group S₅. Sole author.</sub>
<br><a href="https://arxiv.org/abs/2606.12966"><img src="https://img.shields.io/badge/arXiv-2606.12966-B31B1B?style=flat-square&logo=arxiv&logoColor=white&labelColor=21262d" height="24" alt="arXiv:2606.12966" /></a>

**Adaptive Compute in Latent World Models: When Depth Helps, Hurts, or Doesn't Matter**
<br><sub>Pre-registered study of adaptive-depth latent world models across nine DeepMind Control tasks. Maps when extra depth helps rollouts (ρ up to **4.7×**), when shallow beats deep (**2 of 9** tasks), and the routability catch-22 created by early-exit supervision.</sub>
<br><a href="https://arxiv.org/abs/2607.10203"><img src="https://img.shields.io/badge/arXiv-2607.10203-B31B1B?style=flat-square&logo=arxiv&logoColor=white&labelColor=21262d" height="24" alt="arXiv:2607.10203" /></a>

---

## `$ tail -f ~/blog`

**Research**
- **[We found the moment grokking actually begins](https://blog-blogachyuthan.vercel.app/blog/we-found-the-moment-grokking-actually-begins)** — the FSD preprint in plain English: circuits form 500–3,000 steps before the accuracy jump.
- **[When depth helps, hurts, or doesn't matter](https://blog-blogachyuthan.vercel.app/blog/when-more-compute-doesnt-help-adaptive-compute-latent-world-models)** — a taxonomy of adaptive compute in latent world models.

**From the trenches**
- **[When resuming training made my model learn the wrong data](https://blog-blogachyuthan.vercel.app/blog/when-resume-training-learns-wrong-data-megatron-bridge)** — the epoch-aware sampler bug behind Megatron-Bridge #4601.
- **[When Docker cache lies](https://blog-blogachyuthan.vercel.app/blog/when-docker-cache-lies-vllm)** — the BuildKit quirk behind a vLLM nightly build failure.

<sub>More at **[blog-blogachyuthan.vercel.app](https://blog-blogachyuthan.vercel.app)**</sub>

---

## `$ cat ~/.now`

**Building**
- **AD-LiST-JEPA** — spatiotemporal JEPA world model for autonomous driving; predicts future BEV LiDAR embeddings without labels or contrastive pairs
- **KAN-Multi** — routing layer that selects among 6 function bases with zero supervision; **+6.8% over MLP** on CIFAR-100
- **MoE-Bench** — open diagnostic toolkit for expert collapse & routing entropy in sparse MoE LLMs (OLMoE, JetMoE, Qwen)

**Focus** &nbsp;·&nbsp; Self-supervised learning · Sparse MoE architectures · Neural routing · World models · LiDAR perception

**Stack**
<br/>
<img src="https://img.shields.io/badge/Python-21262d?style=flat-square&logo=python&logoColor=3776AB&labelColor=21262d" height="26" alt="Python" />
<img src="https://img.shields.io/badge/PyTorch-21262d?style=flat-square&logo=pytorch&logoColor=EE4C2C&labelColor=21262d" height="26" alt="PyTorch" />
<img src="https://img.shields.io/badge/C%2B%2B-21262d?style=flat-square&logo=cplusplus&logoColor=00599C&labelColor=21262d" height="26" alt="C%2B%2B" />
<img src="https://img.shields.io/badge/Go-21262d?style=flat-square&logo=go&logoColor=00ADD8&labelColor=21262d" height="26" alt="Go" />
<img src="https://img.shields.io/badge/HuggingFace-21262d?style=flat-square&logo=huggingface&logoColor=FFD21E&labelColor=21262d" height="26" alt="HuggingFace" />
<img src="https://img.shields.io/badge/Docker-21262d?style=flat-square&logo=docker&logoColor=2496ED&labelColor=21262d" height="26" alt="Docker" />
<img src="https://img.shields.io/badge/FastAPI-21262d?style=flat-square&logo=fastapi&logoColor=009688&labelColor=21262d" height="26" alt="FastAPI" />
<img src="https://img.shields.io/badge/AWS-21262d?style=flat-square&labelColor=21262d" height="26" alt="AWS" />

---

## `$ open portfolio`

<div align="center">
  <a href="https://achyuthan-s.web.app" target="_blank">
    <img src="https://raw.githubusercontent.com/Achyuthan-S/Achyuthan-S/main/portfolio_preview.jpeg" width="820" alt="Portfolio preview" />
  </a>
  <br/><br/>
  <a href="https://achyuthan-s.web.app" target="_blank"><strong>→ achyuthan-s.web.app</strong></a>
</div>

---

## `$ ./connect`

📫 [as21154@nyu.edu](mailto:as21154@nyu.edu) &nbsp;·&nbsp; [achyuthan.sivasankar@gmail.com](mailto:achyuthan.sivasankar@gmail.com) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/achyuthan-sivasankar-b0814b221) &nbsp;·&nbsp; [Portfolio](https://achyuthan-s.web.app) &nbsp;·&nbsp; [Blog](https://blog-blogachyuthan.vercel.app)
