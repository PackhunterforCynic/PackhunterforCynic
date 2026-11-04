with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

cli_css = '''
    /* Interactive Terminal CLI Input */
    .interactive-cli-line {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 10px;
      padding-top: 8px;
      border-top: 1px dashed #22272E;
    }
    #cli-input {
      background: transparent;
      border: none;
      outline: none;
      color: #00F2FE;
      font-family: var(--font-mono);
      font-size: 11.5px;
      flex: 1;
    }
    #cli-input::placeholder {
      color: #484F58;
    }
    #cli-output {
      margin-top: 8px;
      font-family: var(--font-mono);
      font-size: 11px;
      line-height: 1.5;
      color: #8B949E;
      max-height: 140px;
      overflow-y: auto;
      padding-right: 4px;
    }
    #cli-output div { margin-bottom: 4px; }
    #cli-output a { color: #00F2FE; text-decoration: none; font-weight: 700; }
    #cli-output a:hover { text-decoration: underline; color: #39F59A; }
'''

if '/* Interactive Terminal CLI Input */' not in c:
    c = c.replace('/* Background Canvas */', cli_css + '\n    /* Background Canvas */')

cli_html = '''              <div class="interactive-cli-line">
                <span class="t-prompt">➜</span> <span class="t-path">~/terminal</span>
                <input type="text" id="cli-input" placeholder="Type command ('help', 'projects', 'skills', 'wolf', 'clear')..." autocomplete="off" />
              </div>
              <div id="cli-output"></div>
            </div>'''

old_term_end = '''              <div>
                <span class="t-tag">[STATUS]</span> <span class="t-success">✔ 200 OK — 24 Verified Repositories &amp; 6 Production Demos Online</span>
              </div>
            </div>'''

new_term_end = '''              <div>
                <span class="t-tag">[STATUS]</span> <span class="t-success">✔ 200 OK — 24 Verified Repositories &amp; 6 Production Demos Online</span>
              </div>
''' + cli_html

if 'id="cli-input"' not in c:
    c = c.replace(old_term_end, new_term_end)

cli_js = '''
    // 4. Interactive Terminal CLI Evaluator
    const cliInput = document.getElementById('cli-input');
    const cliOutput = document.getElementById('cli-output');

    if (cliInput) {
      cliInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const cmd = cliInput.value.trim().toLowerCase();
          cliInput.value = '';
          executeCommand(cmd);
        }
      });
    }

    function executeCommand(cmd) {
      if (!cmd) return;
      playBeep(750, 0.05);
      const row = document.createElement('div');
      
      if (cmd === 'help') {
        row.innerHTML = `<span style="color:#39F59A">Available commands:</span><br>` +
          `• <span style="color:#00F2FE">projects</span> : List all 6 verified production engines with live links<br>` +
          `• <span style="color:#00F2FE">skills</span>   : Core engineering architecture and capabilities<br>` +
          `• <span style="color:#00F2FE">wolf</span>     : Awaken Cyber Wolf AI vector core with sound<br>` +
          `• <span style="color:#00F2FE">audio</span>    : Toggle Web Audio synthesizer sound FX<br>` +
          `• <span style="color:#00F2FE">matrix</span>   : Trigger hyper-speed matrix code rain<br>` +
          `• <span style="color:#00F2FE">contact</span>  : Display direct communication uplink channels<br>` +
          `• <span style="color:#00F2FE">clear</span>    : Clear terminal screen`;
      } else if (cmd === 'projects') {
        row.innerHTML = `<span style="color:#39F59A">⚡ Production Flagship Engines:</span><br>` +
          `1. 📡 <a href="https://musica-apvs.vercel.app" target="_blank">Musica Audio Platform</a> — Zero-DB WebRTC &amp; WebSockets<br>` +
          `2. 🎮 <a href="https://game-rovenor.vercel.app" target="_blank">Ben 10 Battle Arena</a> — Phaser 4 P2P Multiplayer<br>` +
          `3. 🌱 <a href="https://robinsonj.vercel.app" target="_blank">PlantSense AI</a> — Gemini Vision AI &amp; ChromaDB RAG<br>` +
          `4. 📷 <a href="https://robinsonj.vercel.app" target="_blank">CAMX Digital Optics</a> — Real-Time Optics Simulation<br>` +
          `5. 🎥 <a href="https://havilah-alpha.vercel.app" target="_blank">Havilah Studio</a> — Bun Runtime &amp; GSAP Tweens<br>` +
          `6. 🎬 <a href="https://hse-indol.vercel.app" target="_blank">HSE Media Suite</a> — Next.js 15 App Router (Lighthouse 99)`;
      } else if (cmd === 'skills') {
        row.innerHTML = `<span style="color:#39F59A">🧠 Core Engineering Arsenal:</span><br>` +
          `• Languages: TypeScript, JavaScript, Python, C++, SQL, HTML5/CSS3<br>` +
          `• Real-Time: WebRTC (PeerConnection, DataChannel), WebSockets, Socket.IO<br>` +
          `• AI/ML: Gemini Multimodal Vision API, ChromaDB Vector RAG, Python FastAPI<br>` +
          `• Engines: Phaser 4 2D, Web Audio API DSP, Next.js 15, Tailwind v4, Docker`;
      } else if (cmd === 'wolf') {
        playBootChord();
        row.innerHTML = `<pre style="color:#00F2FE; font-size:10px; line-height:1.2;">` +
          `      /\\___/\\      CYBER WOLF AI CORE ONLINE\\n` +
          `     (  o.o  )     "Packhunter for Cynic"\\n` +
          `      >  ^  <      Zero Latency • Maximum Throughput\\n` +
          `     /       \\     Identity: Robinson J. [MCA '25]\\n` +
          `    (___)_(___)` +
          `</pre>`;
      } else if (cmd === 'audio') {
        toggleAudioSynth();
        row.innerHTML = `<span style="color:#39F59A">Audio synthesizer toggled!</span>`;
      } else if (cmd === 'matrix') {
        row.innerHTML = `<span style="color:#00F2FE">⚡ Hyper-Speed Matrix Stream Engaged!</span>`;
        for (let i = 0; i < cols; i++) ypos[i] = Math.random() * h;
        playBeep(1200, 0.15);
      } else if (cmd === 'contact') {
        row.innerHTML = `<span style="color:#39F59A">📡 Uplink Channels:</span><br>` +
          `• Email: <a href="mailto:robinson30122000@gmail.com">robinson30122000@gmail.com</a><br>` +
          `• LinkedIn: <a href="https://linkedin.com/in/robinson-mj" target="_blank">linkedin.com/in/robinson-mj</a><br>` +
          `• GitHub: <a href="https://github.com/PackhunterforCynic" target="_blank">github.com/PackhunterforCynic</a>`;
      } else if (cmd === 'clear') {
        cliOutput.innerHTML = '';
        return;
      } else {
        row.innerHTML = `<span style="color:#FF5F56">Command not recognized: '${cmd}'. Type '<span style="color:#00F2FE">help</span>' for options.</span>`;
      }
      
      cliOutput.appendChild(row);
      cliOutput.scrollTop = cliOutput.scrollHeight;
    }
'''

if 'executeCommand' not in c:
    c = c.replace('  </script>', cli_js + '\n  </script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Updated index.html with interactive CLI!')
