# Setup & Publishing Guide — GitHub Profile Repository

This guide details how to publish this profile repository to your special GitHub profile repository: **`PackhunterforCynic/PackhunterforCynic`**.

---

## 1. Prerequisites

- A GitHub account: [`PackhunterforCynic`](https://github.com/PackhunterforCynic)
- Git installed on your system (verified: `git version 2.53.0.windows.1`)
- A GitHub Personal Access Token (classic with `repo` and `workflow` scopes) OR GitHub CLI (`gh`).

---

## 2. Step-by-Step Publishing Process

### Step 1: Create the Special Repository on GitHub
1. Open your browser and go to: **[https://github.com/new](https://github.com/new)**
2. In the **Repository name** field, type exactly:
   ```text
   PackhunterforCynic
   ```
   > 💡 GitHub will display a banner: *"You found a secret! PackhunterforCynic/PackhunterforCynic is a special repository that you can use to add a README.md to your GitHub profile."*
3. Set visibility to **Public** *(critical: private repositories will not render on your public profile)*.
4. **Do NOT check** "Add a README file", ".gitignore", or "license" (we already have all files created locally).
5. Click **Create repository**.

---

### Step 2: Initialize & Push from Local Workspace

Open PowerShell in `d:\Robinson\PROJECTS\git-profile`:

```powershell
# 1. Initialize git repository
git init -b main

# 2. Add all profile files
git add .

# 3. Commit the redesign
git commit -m "feat: initial release of premium developer profile and visual branding"

# 4. Add the GitHub remote
git remote add origin https://github.com/PackhunterforCynic/PackhunterforCynic.git

# 5. Push to GitHub
git push -u origin main
```

*(If prompted for credentials, use your GitHub username `PackhunterforCynic` and your GitHub Personal Access Token as the password).*

---

### Step 3: Enable GitHub Actions Permissions for Contribution Snake

The repository includes `.github/workflows/snake.yml` to automatically generate the contribution graph snake animation. For this workflow to write to the `output` branch, enable write permissions:

1. On GitHub, navigate to your repository:  
   `https://github.com/PackhunterforCynic/PackhunterforCynic`
2. Click **Settings** (gear tab at the top right).
3. In the left sidebar, click **Actions** ➔ **General**.
4. Scroll down to **Workflow permissions**.
5. Select **Read and write permissions**.
6. Check the box **Allow GitHub Actions to approve pull request requests** (optional, recommended).
7. Click **Save**.

---

### Step 4: Trigger the First Snake Workflow Run

1. In the repository, click the **Actions** tab.
2. Under "All workflows" on the left, click **Generate Contribution Snake Animation**.
3. Click the **Run workflow** dropdown button on the right.
4. Keep `Branch: main` and click **Run workflow**.
5. Wait ~45 seconds for the job to complete. It will automatically build and publish the snake SVGs to an `output` branch.
6. Refresh your main profile page: **[https://github.com/PackhunterforCynic](https://github.com/PackhunterforCynic)**.

---

## 3. GitHub Profile Account Optimization Checklist

To ensure maximum impact for recruiters and technical leaders, update your GitHub account settings at:  
👉 **[https://github.com/settings/profile](https://github.com/settings/profile)**

- [ ] **Name:** Change from `Robinson` to **`Robinson J.`**
- [ ] **Bio (Max 160 chars):**  
  ```text
  Software Engineer & Systems Architect | Real-Time Systems, WebRTC, AI Vision & Full-Stack Engineering (MCA '25)
  ```
- [ ] **Location:** `Bengaluru, India`
- [ ] **Website:** `https://robinsonj.vercel.app`
- [ ] **Social Accounts:**
  - LinkedIn: `https://linkedin.com/in/robinson-mj`
- [ ] **Pinned Repositories:**  
  Pin your top 6 repositories on your profile:
  1. `musica` (Real-Time Audio & WebRTC Screen Broadcast)
  2. `game` (Ben 10: Alien Battle Arena - Phaser 4 / React 19 / P2P)
  3. `hse` (Multimedia Production Engine - Next.js)
  4. `hse1` (Full-Stack Agency Web Application)
  5. `havilah` (Multimedia Studio)
  6. `robisnon` (Personal Developer Portfolio)

