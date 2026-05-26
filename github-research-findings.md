# GitHub Research Findings
*Non-technical tools useful for Adam Dak — real estate wholesaling, Cairo, Claude Code Agentic OS*

---

## github.com/topics/real-estate -- 2026-05-26

*40 repos scored across 2 pages (sorted by stars). Ruthless filter: dev/ML/scraper/infra repos all cut. 4 new qualifying tools found.*

### Found (7+)

- **AlpacaLabsLLC/skills-for-architects** (156★) — Score **9**. "Claude Code skills for architecture, real estate, and workplace strategy." Pre-built Claude Code skill set targeting RE professionals — not dev skills, but actual operational skills for real estate work (space planning, property strategy, workplace decisions). Real estate angle: Adam runs Claude Code as his Agentic OS; installing these skills drops pre-wired RE workflows directly into his command palette. Could include deal analysis templates, comp research flows, or client communication drafts. Exact skill inventory needs inspection but the target audience (RE + non-dev) is spot-on. Zero build effort — just install.

- **prolinkinfo/RealEstateCRM** (318★) — Score **8**. "CRM: Empowering Real Estate Agents with Modern CRM Tools." Open-source CRM purpose-built for real estate — lead tracking, deal pipeline, contact management, follow-up reminders. Built for RE agents/closers, not generic sales. Real estate angle: Adam's core tool as a remote closer is a CRM; most paid options (HubSpot, Podio, Follow Up Boss) cost $30-$200/month. This is self-hostable via a standard web stack and designed around RE-specific workflows (leads → motivated sellers → offers → under contract → closed). Inspect whether it handles wholesaling pipeline stages or can be configured for it.

- **etewiah/awesome-real-estate** (314★) — Score **7**. "Curated list of awesome real estate related resources and projects." Aggregated directory of RE tools, APIs, datasets, platforms, and OSS projects — the meta-resource. Real estate angle: Adam's research sessions produce findings one topic at a time; this list could surface 10-20 additional non-technical RE tools in one scan. Includes sections on property data APIs, valuation tools, CRM software, and investment calculators. Worth one dedicated review session to mine it for Adam-relevant picks before moving to other GitHub topics.

- **AleksNeStu/ai-real-estate-assistant** (193★) — Score **7**. "AI platform with conversational property search and analytics." AI-powered conversational interface layered over property data — ask natural-language questions about properties, get structured analytics back. Real estate angle: useful for US market comp research, neighborhood analysis, and deal viability checks — the kind of quick-hit research a closer does before a call or after getting a lead address. Not a wholesaling pipeline tool, but a research accelerator that reduces the time between "got a lead" and "have enough data to make an offer."

### Filtered

36 repos — dev/ML/infra:
- **API-mega-list** (5.5k) — developer API reference
- **streamlit-geospatial** (1k) — Python/ML geospatial data science
- **flathunter** (1k) — Python bot, German rental market only
- **HomeHarvest** (684) — Python scraping package
- **property_web_builder** (617) — Rails developer tool
- **fredy** (638) — German property search bot, dev setup required
- **building-sunlight-simulator** (446) — frontend engineering tool
- **real-estate-mcp** (348) — Korea-specific apartment data MCP (market irrelevant)
- **3dio-js** (281) — JavaScript interior-app toolkit
- **real-estate-management** (280) — dev platform (React/Node)
- **PropertyFindAR** (268) — Android architecture sample app
- **loca** (240) — PHP/self-hosted landlord mgmt, requires dev deploy
- **movinin** (207) — rental property mgmt app, requires dev deploy
- **daftlistings** (189) — Python library for Irish property site
- **hdb-price-predictor** (179) — ML/Streamlit, Singapore HDB only
- **ResidenceCMS** (178) — PHP/Symfony CMS, dev deploy
- **Predicting_real_estate_prices** (176) — ML regression, dev/Jupyter
- **online-rental-property-manager** (174) — landlord mgmt (not wholesaling)
- **Hozn-RealEstate-Fullstack** (159) — MERN stack dev project
- **pyfunda** (143) — Python API wrapper, Dutch market
- **real-estate-ai-agent** (138) — Python/JSON extraction, dev tool
- **property_web_scraper** (116) — scraper UI, dev-adjacent
- **ai-resources** (112) — generic daily-updated AI link dump
- **real-estate-laravel** (106) — Laravel dev project
- **RedfinScraper** (98) — Python Redfin scraper
- **Real-Estate-Website** (92) — MERN stack dev project
- **property-seeker** (89) — Chrome extension (house-hunter, not wholesaler)
- **estatezilla** (88) — PHP CMS, dev deploy
- **Real-Estate-Booking-Website** (86) — MERN stack dev project
- **real_estate_ml** (84) — ML/Jupyter notebooks
- **Real-Estate-Rental-and-Tenant-Management-System** (80) — PHP/dev platform
- **orpms** (79) — PHP RPMS, dev deploy
- **real-estate-neighborhood-prediction** (78) — ML/Python
- **financial_lessons** (725) — passive reading resource, no action lever
- **condo** (346) — property mgmt SaaS, self-hosting overhead, not for wholesaling
- **microrealestate** (1.1k) — landlord/rental mgmt, not wholesaling

---

## github.com/topics/second-brain -- 2026-05-26

*40 repos scored across 2 pages (sorted by stars). 2 skip-list variants (revezone, obsidian-ava). 2 flagged synthetic. 17 new qualifying tools found.*

### Found (7+)

- **smixs/agent-second-brain** (258★) — Score **9**. "Send voice notes to Telegram → get organized knowledge base, tasks in Todoist, and daily reports." Voice memo hits Telegram → agent transcribes → extracts tasks into Todoist, stores knowledge with Ebbinghaus spaced-repetition decay, sends a daily digest. Built by a marketing professional transitioning into AI automation (not a dev tool). Real estate angle: record a 60-second voice note after every seller call → system auto-creates follow-up tasks, files the deal context in PKM, and reminds Adam when to re-contact based on forgetting curves. The Todoist + daily report loop is directly actionable. ~$25/month to run.

- **huytieu/COG-second-brain** (487★) — Score **9**. "Self-evolving second brain with 17 AI skills, 6 worker agents, and people CRM — inspired by Garry Tan's gstack and gbrain." Local-first, Obsidian + Git, no external database, multi-AI-platform (Claude Code, Cursor, Kiro, Gemini CLI). Comes with a built-in people CRM — contacts, relationship notes, follow-up tracking. Real estate angle: 17 pre-built AI skills covering PKM, team intelligence, and PM workflows map directly to deal management; the CRM layer tracks sellers, buyers, and contacts without paying for a separate CRM tool. Everything is markdown files locally owned.

- **Dataojitori/nocturne_memory** (1,100★) — Score **8**. "Lightweight, rollbackable, and visual Long-Term Memory Server for MCP Agents." Persistent, structured memory for AI agents across sessions — graph-based (not vector RAG), with a visual dashboard to inspect and edit what the agent remembers, full version history and rollback. Real estate angle: plugs into Claude Code as an MCP server to give every Claude session persistent memory of deal state, seller history, and Adam's preferences — without re-briefing. The visual dashboard means Adam can see and correct what Claude "knows," which matters when bad data could influence a deal. Complements basic-memory from prior batch.

- **groepl/Obsidian-Templates** (1,700★) — Score **8**. Zettelkasten method templates and scripts for Obsidian — structured note templates for daily notes, literature notes, permanent notes, meeting notes, project notes, and MOCs. All plug-and-play inside Obsidian. Real estate angle: Adam's 246-note vault is live; these templates add structure immediately — a "Seller Call" template that auto-prompts for motivation, timeline, price, condition, and follow-up; a "Deal Note" template that links seller → property → status → tasks. No setup beyond downloading the templates folder. Best immediate wins for vault hygiene.

- **elblogbruno/NotionAI-MyMind** (281★) — Score **8**. "Uses AI and Notion to add web content to your 'Mind' — forget about everything else." Browser-based AI capture that sends any webpage, article, or resource directly to a Notion database, AI-categorized and summarized. No copy-paste. Real estate angle: browsing a county assessor page, a comparable sale, a neighborhood report, or a wholesaling blog post → one click sends it to the deal or research database in Notion, tagged and summarized. Eliminates the "I'll save this to read later" chaos. Works alongside existing Notion setups.

- **ergut/mcp-logseq** (273★) — Score **8**. "MCP server to interact with Logseq via its Local HTTP API — enabling AI assistants like Claude to seamlessly read, write, and manage your LogSeq graph." Logseq is a powerful outliner/journal/PKM app (free, local-first, used by non-developers heavily); this MCP server connects it directly to Claude Code. Real estate angle: if Adam uses Logseq for daily journaling and deal notes, Claude can read entries, create new blocks, update task statuses, and search the graph — all from within a Claude Code session. Turns Logseq into a live context layer for the agentic OS.

- **pbek/QOwnNotes** (5,800★) — Score **7**. "Plain-text file notepad and todo-list manager with Markdown support and Nextcloud / ownCloud integration." Desktop notes app (Windows/Mac/Linux), works with plain Markdown files on disk, syncs via Nextcloud. No cloud lock-in, no subscription, 20+ years of active development. Real estate angle: simple, reliable Markdown notes synced across devices without the complexity of Obsidian's plugin ecosystem. Good fallback or secondary capture app for people overwhelmed by Obsidian's setup overhead. File-compatible with Obsidian.

- **satellitecomponent/Neurite** (2,100★) — Score **7**. "Fractal Graph-of-Thought. Rhizomatic Mind-Mapping for AI Agents, Web-Links, Notes, and Code." Visual canvas where notes, web pages, and AI conversations all live as connected nodes in a fractal/spatial interface. Not a flat list — everything is spatially arranged and linked visually. Real estate angle: ADHD-friendly spatial thinking tool — map out a deal's moving parts (seller → motivation → timeline → comps → offer range → title → exit strategy) as a live visual graph with notes attached. AI agents can navigate and annotate the graph. No cloud required.

- **paperboi/kindle2notion** (964★) — Score **7**. "Export all clippings from your Kindle device to a database in Notion." Automatically pulls all highlights and notes from a Kindle into a clean Notion database — tagged by book, sortable, searchable. Real estate angle: Adam reads real estate books, wholesaling guides, and sales psychology material on Kindle; this converts passive reading highlights into a searchable Notion reference database. Compounds reading investment into actionable reference material. One-time setup, runs on demand.

- **churichard/notabase** (904★) — Score **7**. "A second brain for your knowledge, thoughts, and ideas." Clean, modern note-taking app built specifically around second brain concepts — bidirectional links, backlinks graph, rich text with Markdown. Self-hostable. Real estate angle: simpler than Obsidian with a cleaner interface — useful as a lightweight deal-notes app or for contacts who need shared access to a deal knowledge base. More approachable than Obsidian for non-technical collaborators.

- **dongdongbh/Mindwtr** (871★) — Score **7**. "A complete Getting Things Done (GTD) productivity system for desktop and mobile." Full GTD implementation — inbox, next actions, projects, waiting-for, someday-maybe, weekly reviews — packaged as a cross-platform desktop and mobile app. No code, no plugins. Real estate angle: GTD is the most proven system for managing a high-volume pipeline with interrupts (cold calls, inbound leads, follow-ups, title delays). Weekly reviews prevent deals from dying in the "waiting" folder. More opinionated and structured than a blank Obsidian vault.

- **blueberrycongee/Lumina-Note** (860★) — Score **7**. "Modern Markdown note-taking app with live preview, bidirectional links, and AI assistant." Desktop app — clean UI, AI-assisted writing and summarization built in, bidirectional links for knowledge connections. Real estate angle: fast capture with AI formatting inline — write raw call notes, AI structures them on save; bidirectional links connect the seller note to the deal note to the follow-up note automatically. Good alternative to Obsidian with less setup friction and an AI assistant already integrated.

- **davidmyersdev/octo** (508★) — Score **7**. "A local-first knowledge management app." Minimalist KM app that stores everything locally in the browser's storage (no server needed), Markdown-based, search and tag support. Works offline. Real estate angle: ultra-simple capture and organization — no plugins, no setup, no accounts. Good for a specific use case: a browser-accessible local note system for quick capture at a shared computer or when the main machine isn't available.

- **NicholasSpisak/second-brain** (352★) — Score **7**. "LLM-maintained personal knowledge base for Obsidian. Based on Andrej Karpathy's LLM Wiki pattern." An Obsidian vault structure where an LLM continuously synthesizes, links, and updates entries based on new inputs — the wiki grows and cross-references itself over time. Real estate angle: deal notes and seller research fed into the vault get automatically synthesized into a growing knowledge base — patterns across deals (what seller motivations lead to accepted offers, which counties process title faster) emerge without manual analysis.

- **paulbricman/dual-obsidian-client** (238★) — Score **7**. "A skilled virtual assistant for Obsidian." Obsidian plugin that adds an AI assistant sidebar with access to vault context — ask questions, get answers grounded in your notes, generate new content. By Paul Bricman, a known AI/PKM researcher. Real estate angle: ask "what do I know about this seller?" or "what are all the pending deals in Phoenix?" without leaving Obsidian. AI answers are vault-grounded, not generic. Complements obsidian-ava (already in list) as a different layer — ava for formatting, dual for conversational querying.

- **phuryn/pm-brain** (226★) — Score **7**. "PM Brain OS: The Second Brain for Product Managers, Made of Markdown." A complete Markdown-based second brain system pre-built for operators — project tracking, OKRs, meeting notes, decision logs, stakeholder maps — all in structured templates designed for non-developers managing complex workstreams. Real estate angle: the template structure maps cleanly to wholesaling — replace "product" with "deal," "stakeholders" with "seller/buyer/title/agent," OKRs with monthly offer targets. Download the vault structure, rename the categories, run it in Obsidian. No setup beyond that.

- **vasylenko/bear-notes-mcp** (193★) — Score **7**. "MCP Server for Bear note-taking app — available as Claude Desktop extension or standalone server for any AI tool." Bear is a polished macOS/iOS Markdown note app (paid, ~$30/year). This MCP server lets Claude read, write, and search Bear notes directly in a session. Real estate angle: if Adam uses Bear for mobile capture (clean iPhone UX), this bridges Bear into the Claude Code agentic OS — Claude can pull a seller note from Bear mid-session, update it with new info, and the change syncs to iPhone immediately. Native Apple ecosystem integration.

### Flagged Synthetic (implausible star-to-commit ratios / suspicious accounts)

- **ballred/obsidian-claude-pkm** (1,500★) — "Complete starter kit for Obsidian + Claude Code PKM." Unknown account, 1.5k stars for niche Claude Code–specific PKM starter kit, owner name pattern matches prior synthetic clusters. Skip.
- **lucasrosati/claude-code-memory-setup** (705★) — "Up to 71.5x fewer tokens per session on Claude Code with Obsidian + Graphify." The "71.5x" figure is a synthetic-style precision marketing claim; account unverifiable; 705 stars for a very niche benchmark setup is disproportionate. Skip.
- **AgriciDaniel/claude-obsidian** (5,500★) — already flagged in knowledge-management batch. Reappears here; skip.
- **agenticnotetaking/arscontexta** (3,400★) — already flagged in knowledge-management batch. Reappears here; skip.
- **eugeniughelbur/obsidian-second-brain** (1,400★) — already flagged in knowledge-management batch. Reappears here; skip.

### Filtered

**16 repos** — reason breakdown:

- **Technical setup required / score 4–6:** reorproject/reor (8,600★ — requires Ollama install for local AI), zk-org/zk (2,600★ — CLI plain-text Zettelkasten tool), maximevaillancourt/digital-garden-jekyll-template (1,300★ — Jekyll/dev publishing template), kytmanov/obsidian-llm-wiki-local (653★ — requires Ollama), mathieudutour/gatsby-digital-garden (686★ — Gatsby/dev template), jobindjohn/obsidian-publish-mkdocs (649★ — dev publishing pipeline), davidmyersdev/octo is included above
- **Resource lists only (not tools):** MaggieAppleton/digital-gardeners (4,700★ — list of PKM resources), KasperZutterman/Second-Brain (1,800★ — curated awesome-list), oldwinter/knowledge-garden (2,400★ — personal Obsidian public vault, not a tool)
- **Dev/infra/score 1–3:** ChristianLempa/cheat-sheets (4,800★ — sysadmin cheat sheets), lyz-code/blue-book (958★ — developer personal notes), grumpyp/aixplora (274★ — generic file-querying CLI tool), flepied/second-brain-agent (297★ — vague AI agent stub), costinEEST/almanacs (240★ — recipe search app, off-topic), paulbricman/dual-obsidian-client listed above; see also gatsby above

---

## github.com/topics/knowledge-management -- 2026-05-25

*40 repos scored across 2 pages (sorted by stars). 1 skip-list variant (awesome-openclaw-usecases-zh). 1 defunct (athens). 4 flagged synthetic. 14 new qualifying tools found.*

### Found (7+)

- **basicmachines-co/basic-memory** (3,100★) — Score **9**. "AI conversations that actually remember. Never re-explain your project to your AI again." Persistent memory layer for Claude (and other LLMs) — stores facts, decisions, and context from every conversation as structured Markdown files in a local folder. No re-briefing Claude each session: it already knows Adam's deal pipeline, seller context, call notes, and active strategies from prior sessions. Direct plug for the agentic OS: install basic-memory as an MCP server, point it at the vault, and Claude maintains continuity across every session. This is the missing memory primitive for Adam's setup.

- **TriliumNext/Trilium** (36,200★) — Score **8**. The most powerful self-hosted personal knowledge base available — hierarchical notes with rich text, code blocks, relation maps, scripting, and a full REST API. Not Obsidian (flat files) but a structured tree database. Real estate angle: deal hierarchy (Seller → Property → Notes → Follow-ups → Documents) where every node is searchable and linkable. The AI scripting layer lets you add automation without code via built-in JS hooks. Actively maintained by a fork community after the original author stepped back. Works offline, no subscription.

- **deta/surf** (3,400★) — Score **8**. Personal AI Notebooks — upload files, add URLs, and chat with the resulting knowledge base using an AI assistant. No setup beyond installing the app. Real estate angle: dump a seller's property docs, comparable listings, and call notes into a notebook, then ask "what's the best angle for this offer?" and get context-aware answers. Replaces 20 minutes of re-reading notes before a call. Works as a lightweight alternative to full vector DBs for per-deal research aggregation.

- **freeplane/freeplane** (4,100★) — Score **8**. Mature, free desktop application for mind mapping, knowledge management, and project management — all from a visual node-and-branch interface. No code, no cloud, no subscription. Real estate angle: map out a deal's key facts visually (seller motivation, timeline, property issues, comps, offer strategy), track project milestones with task nodes, and export to PDF for team handoffs. Runs on Windows/Mac/Linux. Better for visual thinkers who find linear lists hard to navigate.

- **revezone/revezone** (2,600★) — Score **8**. Lightweight local-first visual productivity tool for building a second brain — combines a canvas workspace (Excalidraw), markdown notes, and a board interface in one self-contained app. No cloud required. Real estate angle: visual deal maps on canvas (seller situation → offer → title → close path), written notes alongside, without switching between apps. Great for ADHD users who think spatially before linearly. Early-stage but functional.

- **KnowledgeCanvas/knowledge** (1,500★) — Score **8**. Desktop app for saving, searching, accessing, exploring, and chatting with all your files, websites, and documents in a unified AI-powered interface. Import PDFs, add bookmarks, upload notes — then query the whole collection conversationally. Real estate angle: every contract template, county form, comp report, and seller research article lives in one searchable, AI-chattable corpus. Replaces tabbed browser chaos and document folder archaeology. Download and run locally.

- **iwe-org/iwe** (1,100★) — Score **8**. "Markdown memory system for you and your AI agent." Organizes Markdown notes into a structured, queryable memory layer specifically designed for use alongside AI agents — backlinks, transclusions, and structured topic nodes. Real estate angle: deal notes become agent-readable structured memory rather than flat files. Pairs well with Claude Code as the file-layer for persistent context. Similar in spirit to basic-memory but focused on Markdown structure and AI-agent query patterns.

- **different-ai/obsidian-ava** (658★) — Score **8**. Obsidian plugin that uses AI (originally ChatGPT, now supports multiple models) to auto-format, rewrite, summarize, and link notes — directly inside the vault. No copy-pasting between apps. Real estate angle: paste raw call notes → ask AVA to structure them as a deal summary with key facts, follow-up items, and seller sentiment. Pairs with Adam's 246-note Ramp Academy vault and any new deal-tracking notes. Complements claudian (AI-inside-Obsidian) as a formatting and processing layer.

- **silverbulletmd/silverbullet** (5,300★) — Score **7**. Open-source personal productivity platform built on Markdown with a Lua scripting engine for automation. Works like a programmable Obsidian — live queries, slash commands, and event hooks. Real estate angle: define a "Deal Note" template that auto-creates follow-up tasks, query all open deals with a live filtered list, and run custom automation on note save. Non-technical for basic use; scripting only needed for advanced customization. Self-hostable web app — works from any browser.

- **zmister2016/MrDoc** (3,200★) — Score **7**. Self-hosted online document system for individuals and small teams to manage wikis, docs, knowledge bases, and notes — clean UI, full Markdown support, permission controls. Real estate angle: shared knowledge base for deal SOPs (how to run a comp, how to fill a contract), seller scripts, objection responses, and onboarding material for future VAs. Confluence-level functionality without the Confluence price. Chinese-developed but English interface.

- **documize/community** (2,400★) — Score **7**. Modern open-source Confluence alternative — structured spaces for internal documentation, wikis, and team knowledge with access controls. Designed for teams but works for solo operators too. Real estate angle: build an operations wiki (seller scripts, county-specific processes, VA playbooks, deal tracking SOPs) that's searchable and version-controlled. If Adam ever hires a VA or brings in a partner, this is the knowledge handoff layer. Self-hosted, no per-seat costs.

- **tiddly-gittly/TidGi-Desktop** (2,000★) — Score **7**. Privacy-focused, automated knowledge management desktop app built on TiddlyWiki with Git sync for version control. TiddlyWiki is a uniquely non-linear knowledge system — every note is a "tiddler" that links, embeds, and filters dynamically. Real estate angle: build a non-linear deal wiki where every property, seller, buyer, and contact is a tiddler linked to related deals, phone logs, and offer history. High learning curve upfront; very powerful once set up. Suits those who find Obsidian too flat.

- **quillpad/quillpad** (1,300★) — Score **7**. Beautiful mobile-first Markdown notes app with task lists, open-source and self-hostable (Nextcloud integration). Real estate angle: capture deal notes and follow-up tasks from the phone immediately after a seller call, synced to the main knowledge base. Fills the gap between desktop Obsidian and mobile capture — better than the default Obsidian mobile app for quick on-the-go capture. Free, no cloud lock-in.

- **brettkromkamp/awesome-knowledge-management** (831★) — Score **7**. Curated list of knowledge management tools, frameworks, apps, and resources — organized by category with descriptions. Not a tool itself but the fastest way to discover what's in the KM space before committing to a system. Real estate angle: browse the PKM tool landscape, find niche tools (like Zettelkasten apps or local AI search) that fit specific gaps in Adam's setup. Good quarterly reference to catch emerging tools before they hit mainstream discovery.

### Flagged Synthetic (implausible star counts / suspicious account patterns)

- **AgriciDaniel/claude-obsidian** (5,500★) — "Claude + Obsidian knowledge companion based on Karpathy's LLM Wiki pattern." Unknown org, 5.5k stars for a niche Claude/Obsidian integration, description echoes multiple synthetic repos found across prior batches. Skip.
- **agenticnotetaking/arscontexta** (3,400★) — "Claude Code plugin that generates individualized knowledge systems from conversation." Unknown org with a purpose-built name, 3.4k stars for a very niche Claude Code plugin, no verifiable community. Skip.
- **eugeniughelbur/obsidian-second-brain** (1,300★) — "Cross-CLI skill for Obsidian transforms vaults into AI-first systems." Suspiciously specific Claude Code–adjacent description, unknown account, star count disproportionate. Skip.
- **Astro-Han/karpathy-llm-wiki** (919★) — "LLM wiki compatible with AI agent skills." Echoes the claude-obsidian repo's "Karpathy LLM Wiki" framing; likely same synthetic cluster. Skip.

### Filtered

**22 repos** — reason breakdown:

- **Defunct:** athensresearch/athens (6,300★) — project discontinued, no longer maintained
- **Skip-list variant:** AlexAnys/awesome-openclaw-usecases-zh (4,200★) — Chinese resource guide for OpenClaw, which is already on skip list
- **Dev/infra/ML tools (score 1–3):** campfirein/byterover-cli (4,800★ — CLI memory layer for coding agents), myhhub/KnowledgeGraph (1,700★ — NLP/ML knowledge graph construction), feenkcom/gtoolkit (1,500★ — moldable dev environment), protegeproject/protege (1,400★ — academic ontology editor), phodal/ledge (2,200★ — DevOps knowledge platform), protegeproject/webprotege (748★ — web ontology editor for academic RDF/OWL), mfarragher/obsidiantools (557★ — Python package for vault analysis), phmullins/awesome-macos-commandline (645★ — macOS CLI tool list)
- **Technical setup required / score 4–6:** iamgio/quarkdown (15,100★ — academic publishing/LaTeX alternative), haiwen/seafile (14,800★ — self-hosted file server requiring server admin), GitJournal/GitJournal (4,200★ — Git-integrated mobile notes, Git knowledge needed), suziwen/markdownxiaoshujiang (1,700★ — Chinese notes app, limited English), dvorka-oss/mindforger (2,700★ — heavy C++ Markdown editor, complex setup), SemanticMediaWiki (608★ — MediaWiki extension for semantic web), unigraph-dev/unigraph-dev (764★ — local knowledge graph, developer-heavy), steven-jianhao-li/zotero-AI-Butler (1,300★ — Zotero plugin for academic paper summaries), felixhayashi/TW5-TiddlyMap (905★ — TiddlyWiki plugin for visualization), rockbenben/LearnData (513★ — blog/notebook template), osmoscraft/osmosmemo (492★ — GitHub-based bookmarking tool), winstonkoh87/Athena-Public (494★ — "Linux OS for AI Agents," requires Linux admin)

---

## github.com/topics/automation -- 2026-05-24

*60 repos scored across 3 pages. 8 already on skip list (n8n, dify, huginn, career-ops, sim, maxun, automatisch, MoneyPrinterTurbo). 3 flagged synthetic. 5 new qualifying tools found.*

### Found (7+)

- **AutomaApp/automa** (21,300★) — Score **8**. Browser extension for no-code browser automation via visual block connections. Zero code: drag blocks, set triggers, chain actions. Real estate angle: automate repetitive web tasks — check Zillow listings, fill CRM forms, copy-paste data from sites, monitor leads. Chrome/Firefox, totally free. One of the cleanest no-code automation tools that works inside the browser itself, no server needed.

- **enescingoz/awesome-n8n-templates** (22,400★) — Score **8**. 280+ free ready-to-use n8n workflow templates covering Gmail, Telegram, Slack, Discord, WhatsApp, and more. Since n8n is already a known find, this is the shortcut library for it — skip building workflows from scratch. Import a template, connect accounts, done. Real estate angle: pre-built email follow-up chains, lead notification routing, CRM sync automations.

- **assafelovic/gpt-researcher** (27,300★) — Score **7**. Autonomous AI research agent — give it a question, it deep-dives the web and returns a full structured research report. No code to run it (web UI available). Real estate angle: research comps in a zip code, pull info on a seller's neighborhood, analyze market trends for a pitch. Saves hours of manual Googling per deal.

- **Skyvern-AI/skyvern** (21,700★) — Score **7**. AI that navigates and automates real browser workflows — fills forms, extracts data, clicks through multi-step flows, without writing code. YC-backed, actively maintained. Real estate angle: automate lead list scraping, property data extraction, form submissions to county portals. Non-technical: describe the task, Skyvern does it.

- **nanobrowser/nanobrowser** (13,000★) — Score **7**. Open-source Chrome extension giving an AI agent control of your browser — similar to Skyvern but runs locally in the extension. Non-technical: type what you want done, the agent browses and does it. Real estate angle: pull comps, check multiple listing sites, monitor price drops on target properties. No server, no code — just install and use.

### Flagged Synthetic (star counts implausible for repo type)

- **ComposioHQ/awesome-claude-skills** (61,600★) — Actual Composio repo is ~10k stars; 61.6k for a curated list is suspicious. Skip.
- **wshobson/agents** (35,900★) — "Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor, OpenCode, and Gemini CLI" — 35.9k for a niche CLI marketplace is implausible. Skip.
- **Yeachan-Heo/oh-my-claudecode** (34,700★) — "Teams-first multi-agent orchestration for Claude Code" — 34.7k for a Claude Code orchestration tool is implausible. Skip.

### Filtered

49 repos filtered — reason breakdown:
- **Dev/infra/testing tools (score 1-2):** puppeteer, playwright, airflow, bruno, fastlane, vagrant, kestra, watchtower, Tasmota, semantic-release, crawlee, prefect, appium, appium, Auto.js, undetected-chromedriver, Detox, webhook, robotframework, RD-Agent, awx, trigger.dev, phantomjs, hammerspoon, ArchiSteamFarm
- **Gaming/social bots (score 1-3):** InstaPy, ArchiSteamFarm, MoneyPrinterV2, MoneyPrinter (YouTube Shorts), ai-goofish-monitor
- **Score 4-6 / requires dev setup:** appsmith, Jobs_Applier_AI_Agent_AIHawk, leon, Obtainium, AutoHotkey, Archon, taipy, googleworkspace/cli, posting, ai-website-cloner-template, Panniantong/Agent-Reach
- **Already on skip list:** n8n, dify, huginn, career-ops, sim, maxun, automatisch, MoneyPrinterTurbo

---

## github.com/topics/productivity -- 2026-05-24

*60 repos scored across 3 pages. 1 on skip list (khoj). 1 already in findings (ShareX). 2 flagged synthetic (see below). 12 new qualifying tools found.*

### Found (7+)

- **YishenTu/claudian** (11,800★) — Score **9**. Obsidian plugin that embeds Claude Code as a live AI collaborator inside your vault — Claude reads, searches, and writes your notes without leaving Obsidian. Direct bridge between Adam's 246-note vault and his Claude Code agentic OS. THE most relevant Claude Code + Obsidian integration available. If Adam is already using both tools, this merges them.

- **super-productivity** (19,600★) — [github.com/johannesjo/super-productivity](https://github.com/johannesjo/super-productivity) — Score **8**. Advanced todo list with timeboxing, time tracking, and Jira/GitHub/GitLab integrations. ADHD-designed: tasks can't sprawl — they get time-boxed. Pomodoro built in. Real estate angle: track call sessions, cap time per deal, log daily prospecting output. Free, desktop + web, zero code. Arguably the most ADHD-compatible open-source task manager that exists.

- **danielmiessler/Personal_AI_Infrastructure** (14,400★) — Score **8**. Daniel Miessler's personal agentic AI setup — his actual prompts, configs, and architecture for using AI to amplify human capabilities, not just answer questions. Not software to install but a living reference blueprint. Directly relevant for Adam building his own Claude Code agentic OS: steal what applies, skip what doesn't. Real person, real usage.

- **rowboatlabs/rowboat** (14,300★) — Score **8**. Open-source AI coworker with persistent memory — designed to function as a perpetual work partner across sessions, not a single-query chatbot. Relevant for building a deal memory layer: stores what Adam knows about sellers, tracks follow-up timing, remembers context between calls. Self-host or cloud.

- **elie222/inbox-zero** (10,900★) — Score **8**. Open-source AI email assistant targeting inbox zero. Auto-categorizes, bulk-unsubscribes, archives low-priority mail, and drafts replies. If Adam's real estate comms flow through Gmail, this is a direct upgrade — reduces email processing time from daily grind to minutes. Actively maintained.

- **ykdojo/claude-code-tips** (8,500★) — Score **8**. Curated tips and techniques for Claude Code usage and workflow efficiency — not a library but actionable guidance. Directly useful for Adam's agentic OS: what to expect, how to prompt effectively, known pitfalls. The author (ykdojo) makes Claude Code tutorials publicly.

- **heilcheng/awesome-agent-skills** (5,100★) — Score **8**. Directory of tutorials and agent skills for AI automation. Supplements Adam's existing awesome-claude-code-subagents research — surfaces reusable skills for non-dev tasks like web research, email drafting, and file management.

- **excalidraw/excalidraw** (124,000★) — Score **7**. Virtual whiteboard with hand-drawn aesthetic — browser-based, no login required. Useful for mapping deal pipelines visually, sketching call scripts, or laying out a seller's situation before a negotiation. Free, instant, works anywhere.

- **ActivityWatch/activitywatch** (17,700★) — Score **7**. Automated local time tracker — runs silently and shows exactly where computer time goes. ADHD-relevant: reveals distraction patterns, protects focus blocks, gives honest data on actual work time vs. perceived. No cloud, privacy-first, free.

- **espanso/espanso** (13,900★) — Score **7**. Cross-platform text expander — type a short trigger, get a full template. Real estate wholesaling angle: type `:offer` → full cash offer template, `:followup` → follow-up script, `:objection1` → price objection response. Zero code to configure (YAML). Massive time-saver for repetitive outreach.

- **rockbenben/ChatGPT-Shortcut** (8,500★) — Score **7**. AI prompt shortcut manager — curated prompts organized by role and task. Browse, copy, and organize prompts for AI workflows. Useful for building Adam's prompt library: deal analysis, seller conversation frameworks, email drafts. Works with any AI, not just ChatGPT.

- **JerryZLiu/Dayflow** (6,000★) — Score **7**. Automatic AI work journal — logs what you worked on and generates a private timeline. ADHD accountability tool: end-of-day summary of what actually got done vs. what was planned. Local-first, AI-generated, no manual input needed.

### Filtered

**46 repos** — dev/ML/infra/shell/CLI/browser-dev: ohmyzsh (187k★), rtk-ai/rtk (53k★), it-tools (39k★), yazi (38k★), plotly/dash (24k★), nnn (21k★), waveterm (20k★), Kap (19k★), screenity (18k★), awesome-python-applications (17k★), omnivore (16k★), Bash-it (15k★), Flow-Launcher (14k★), Zettlr (13k★), shell_gpt (12k★), nyxt (10k★), Loop/macOS-window-mgmt (10k★), omni-tools (9k★), Mac-CLI (9k★), nb/CLI-notes (8k★), vicinae (7k★), omni/Chrome-ext (7k★), oh-my-bash (7k★), opencommit (7k★), jrnl (7k★), massCode (6k★), linearmouse (6k★), passbolt_api (5k★), Clipboard-mgr (5k★), ponzu-cms (5k★), tuist/iOS (5k★), jira-cli (5k★), OctoLinker (5k★), planify/GNOME (5k★), tasks/Android (5k★), MeetingBar/macOS (5k★), pomotroid (5k★), notion-enhancer (5k★), PasteMD (4k★), nylas-mail (24k★ — abandoned), files-community/Files (43k★ — Windows file mgr), drawnix (13k★ — whiteboard clone), notesnook (14k★ — encrypted notes, niche fit)

**2 flagged synthetic** — star counts inconsistent with project scope:
- affaan-m/ECC (190k★) — "agent harness performance optimization for Claude Code" — 190k would rank it among GitHub's most-starred repos ever; description is generic; almost certainly inflated.
- DayuanJiang/next-ai-draw-io (29k★) — Next.js + draw.io fork; 29k for a niche single-integration project is implausible; skip.

---

## github.com/topics/no-code -- 2026-05-24

*40 repos scored across 2 pages. 6 already on skip list (n8n, dify, nocodb, AnythingLLM, Flowise, ToolJet). 26 filtered as dev/infra. 8 new qualifying tools found.*

### Found (7+)

- **automatisch** (13,900★) — [github.com/automatisch/automatisch](https://github.com/automatisch/automatisch) — Score **8**. Open-source Zapier alternative — drag-and-drop visual automation between apps with no code. Connect CRM, email, Google Sheets, Twilio, WhatsApp, and 100+ services into trigger-action workflows. Real estate angle: auto-route inbound leads from a web form → Google Sheet → SMS notification → CRM entry, zero API keys needed. Self-hostable, perpetual free. Closest open-source equivalent to Zapier.

- **simstudioai/sim** (28,600★) — [github.com/simstudioai/sim](https://github.com/simstudioai/sim) — Score **8**. Visual AI agent builder — drag-and-drop canvas to compose multi-step AI workflows and deploy autonomous agents. Describes itself as "the central intelligence layer for your AI workforce." No code required for assembly; models are swappable. Relevant for building a deal-research agent, a follow-up drip agent, or a CRM-feeding pipeline. Cloud + self-host.

- **getmaxun/maxun** (15,600★) — [github.com/getmaxun/maxun](https://github.com/getmaxun/maxun) — Score **8**. No-code web scraping and AI data extraction platform. Point-and-click to define what to scrape; exports to spreadsheets or webhooks. Real estate wholesaling angle: scrape Zillow FSBO listings, probate court public records, or foreclosure feeds without writing code. Converts scraped data to structured tables. Directly useful for list-building.

- **teable** (21,300★) — [github.com/teableio/teable](https://github.com/teableio/teable) — Score **8**. Next-generation Airtable alternative on top of Postgres — spreadsheet UI, no-code, with real database power underneath. Build a lead pipeline tracker, deal stages board, or contact database with views (grid, kanban, gallery, calendar). Faster and more scalable than Airtable for free. Adam already uses NocoDB (similar category) — Teable is the modern, actively maintained competitor.

- **Budibase** (27,900★) — [github.com/Budibase/budibase](https://github.com/Budibase/budibase) — Score **7**. No-code internal app builder that now includes AI agents and automations. Build operational dashboards, lead-intake forms, or deal-pipeline apps from a drag-and-drop interface connecting to any database or API. Model-agnostic for AI features. Broader than Airtable (custom logic, forms, UIs) but still no-code. Self-hostable or cloud.

- **nocobase** (22,500★) — [github.com/nocobase/nocobase](https://github.com/nocobase/nocobase) — Score **7**. Open-source no-code business system builder with WYSIWYG interface — create custom CRMs, project trackers, or ops dashboards without coding. AI features built in. Aimed squarely at non-technical business operators. Self-hostable. If Adam outgrows Notion/NocoDB for deal tracking, this is the next step up.

- **coze-dev/coze-studio** (20,800★) — [github.com/coze-dev/coze-studio](https://github.com/coze-dev/coze-studio) — Score **7**. ByteDance's open-source visual AI agent development platform — all-in-one canvas to design, test, and deploy AI agents with no code. Supports multi-agent orchestration, tool plugins, and knowledge bases. Cloud version at coze.com is fully hosted (no self-hosting required). Solid choice for building deal-screening or lead-qualification agents visually.

- **dtyq/magic** (4,800★) — [github.com/dtyq/magic](https://github.com/dtyq/magic) — Score **7**. All-in-one AI productivity platform combining agent builder, workflow engine, and collaborative office tools (chat, docs, tasks) in a single self-hosted deployment. Enterprise-grade but open-source. Could replace a fragmented stack of Notion + n8n + ChatGPT with one unified system. Lower star count but architecturally ambitious — worth watching.

### Filtered

**26 repos** — dev/ML/infra, game engine, or UI library; score 1–5:

- **strapi** (72.2k) — headless CMS API framework, developer-only
- **nexu-io/open-design** (51.2k) — Claude Design alternative but dev/designer tool
- **directus** (35.8k) — backend API platform, developer-only
- **GrapesJS** (25.9k) — web builder JavaScript library, developer tool
- **GDevelop** (23.2k) — 2D/3D game engine, zero relevance
- **baidu/amis** (18.9k) — JSON-config frontend framework, developer tool
- **apitable** (15.4k) — API-oriented low-code, more technical than Teable
- **datawhalechina/easy-vibe** (14.5k) — coding course for beginners
- **automatisch** — ✅ FOUND above
- **BuilderIO/mitosis** (13.8k) — component compiler for React/Vue/etc
- **jnMetaCode/agency-agents-zh** (12.8k) — Chinese-market AI roles, language barrier
- **puckeditor/puck** (12.7k) — visual editor for React, developer tool
- **alibaba/formily** (12.5k) — dynamic form framework, developer tool
- **VvvebJs** (8.5k) — drag-and-drop page builder library, developer tool
- **bytedance/flowgram.ai** (8.1k) — workflow framework for building AI platforms, developer SDK
- **buildship-ai/rowy** (6.8k) — low-code backend with cloud functions, requires coding
- **clientIO/joint** (5.3k) — SVG diagramming library, developer tool
- **brick-design** (5.1k) — low-code UI framework, developer tool
- **baserow** (4.9k) — similar to NocoDB (already found); duplicate category
- **Welcome-to-Open-Source** (3.8k) — first PR tutorial, zero utility
- **BuilderIO/figma-html** (3.6k) — converts websites to Figma, designer/dev tool
- **awesome-openclaw-agents** (3.4k) — OpenClaw extension (OpenClaw already on skip list)
- **NetEase/tango** (3.1k) — code-driven low-code, requires codebase
- **gmpetrov/databerry** (2.9k) — LLM agent builder, low traction (sub-3k)
- **silexlabs/Silex** (2.8k) — static site creator, not relevant to wholesaling
- **gridaco/grida** (2.5k) — design platform, designer tool
- **KhazP/vibe-coding-prompt-template** (2.4k) — prompt templates for coding, dev-focused

---

## github.com/topics/agentic-ai -- 2026-05-24

*New source — all 6 original task sources exhausted (githublb.vercel.app persistent 403; EvanLi Top100 all 41 files complete). 20 repos scored.*

### Found (7+)

- **dify** (142,000★) — [github.com/langgenius/dify](https://github.com/langgenius/dify) — Score **9**. No-code/low-code AI workflow and agent builder with a drag-and-drop canvas. Build chatbots, RAG pipelines, and multi-step AI workflows without writing code — 50+ prebuilt tool connectors (web search, document processing, image generation). Could build a deal-sourcing assistant, objection-handler chatbot, or automated follow-up pipeline entirely through the UI. One of the most polished no-code AI platforms on GitHub. Self-hostable.

- **AutoGPT** (184,000★) — [github.com/Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) — Score **7**. AI agent platform with a low-code visual block editor; deploy continuous agents that automate complex multi-step workflows. Has a hosted cloud version (no self-hosting required). Select from pre-built agent templates or compose custom ones. Founded the "autonomous AI agent" category in 2023 — mature, well-maintained. Slightly technical for self-hosting but the hosted option lowers the barrier.

- **agenticSeek** (26,400★) — [github.com/Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek) — Score **6**. Fully local AI agent for autonomous web browsing, research, and task execution — no API keys, no ongoing costs. Useful for ad-hoc deal research or prospecting without burning API credits. Setup requires local install (Docker), so it's borderline for non-devs, but the zero-API-cost angle is a genuine advantage.

- **MaxKB** (21,000★) — [github.com/1Panel-dev/MaxKB](https://github.com/1Panel-dev/MaxKB) — Score **6**. Open-source platform for building internal AI knowledge-base assistants from documents. Upload your call scripts, objection handlers, or deal criteria → deploy a chatbot that answers from your own material. GUI-driven, aimed at business users. Self-hostable. Borderline technical to set up but no ongoing coding needed.

### Flagged Synthetic (suspicious star inflation — verify before using)

- **RuView** (64,700★) — `ruvnet/RuView`: WiFi-to-spatial-intelligence tool. The star count is implausible for the repo's scope and follows the same ruvnet pattern as ruflo below. Flag and skip.
- **ruflo** (54,500★) — `ruvnet/ruflo`: "Agent orchestration for Claude" with 1,489 releases (automated release-pumping). Genuine projects rarely exceed 50–100 releases. Star count is almost certainly inflated.
- **claude-code-best-practice** (54,600★) — `shanraisshan/claude-code-best-practice`: A best-practices guide with 54.6k stars is not credible. Real documentation repos at this scale take years to accumulate.

### Filtered

**16 repos** — dev/ML/infra or already found, score 1–4:

- **Flowise** (53k) — *ALREADY FOUND* (TypeScript batch, 2026-05-19)
- **RAGFlow** (81.1k) — RAG + vector engine; requires infra setup, technical configuration. Score 3.
- **ai-agents-for-beginners** (65.3k) — Microsoft 12-lesson AI agents course. Educational resource, not a deployable tool. Score 4.
- **agents** (35.8k) — `wshobson/agents`: "Claude Code plugin marketplace" with suspicious star count for the repo's age/scope. Flagged as likely synthetic; also dev-tool category even if real. Score 3.
- **PageIndex** (32k) — Vectorless RAG document indexing engine; technical infra. Score 2.
- **CopilotKit** (31.7k) — React + Angular frontend library for embedding AI in web apps. Developer tool. Score 2.
- **agents-course** (28.8k) — HuggingFace agents course. Course content, not a tool. Score 3.
- **composio** (28.4k) — SDK powering tool integrations for AI agents; developer SDK. Score 3.
- **crush** (24.6k) — Charmbracelet's agentic coding CLI (TUI-based). Developer coding tool. Score 3.
- **adk-python** (19.8k) — Google's Python SDK for building AI agents. Requires Python/coding. Score 2.
- **keploy** (17.4k) — API testing + production sandbox platform. Dev/QA tool. Score 2.
- **agent-lightning** (17.2k) — Microsoft RL training framework for AI agents. ML infra. Score 1.
- **RagaAI-Catalyst** (16.2k) — Python SDK for agent observability and monitoring. Dev SDK. Score 2.

---

## EvanLi Top100 — DM + Groovy + Julia + Perl + TeX -- 2026-05-23

### Found (7+)

*None.* Five language lists scanned. All 500 repos score 1–4. Zero qualifying tools for Adam.

### Filtered

**500 repos total** across five languages — all dev/infra/academic:

**DM (100 repos)** — DM is BYOND's in-game scripting language. The *entire* top 100 is Space Station 13 server codebases — a community-run sci-fi roleplaying game. No standalone apps, no productivity tools. Largest: tgstation (1,895★), Paradise (446★), Baystation12 (422★), goonstation (396★). Score 1–2 across all 100.

**Groovy (100 repos)** — Groovy is a JVM scripting language used almost exclusively for Gradle build scripts and Jenkins CI pipelines. The entire list is Gradle plugins, Jenkins pipeline tools, and DevOps infra. Largest: gradle (18,577★), devops-resources (9,537★), rundeck (6,120★). Score 1–3 across all 100. One borderline: **openboxes** (841★, supply-chain management for healthcare) but requires Java server + dev setup — filtered.

**Julia (100 repos)** — Julia is a scientific computing language. The entire list is ML frameworks, differential equations solvers, Bayesian inference packages, quantum computing libraries, and academic course materials. All require Julia installation and domain expertise. Largest: julia (48,729★, the language itself), Flux.jl (4,727★), DifferentialEquations.jl (3,103★). Score 1–3 across all 100.

**Perl (100 repos)** — Perl is a sysadmin/text-processing language. The top 100 is network monitoring tools, security scanners, database admin scripts, and developer utilities. All require CLI/server access. Largest: cloc (23,066★), FlameGraph (19,497★), diff-so-fancy (18,025★), nikto (10,388★, web vulnerability scanner), exiftool (4,702★). Score 1–3 across all 100. One marginal close miss: **git-it-electron** (4,875★) — desktop app for learning Git/GitHub but that's a developer education tool, score 4.

**TeX (100 repos)** — TeX/LaTeX is a typesetting language. The entire list is academic textbooks, ML research paper PDFs, university thesis templates, and LaTeX learning guides. All are read-only documents or require LaTeX installation to generate content. Largest: deeplearningbook-chinese (37,273★), libpku (33,589★), Awesome-CV (27,557★, LaTeX CV template). Score 1–3 across all 100. Marginal filtered: **resumake.io** (3,560★, web-based LaTeX resume generator) — score 5, too niche for current priority since Adam has career-ops; **the-sourdough-framework** (3,565★) — open-source bread-baking book, zero wholesaling relevance.

---

## EvanLi Top100/CoffeeScript.md -- 2026-05-23

### Found (7+)

*None.* CoffeeScript is a programming language — its entire top 100 consists of developer tools, UI libraries, build systems, and frameworks. Zero repos score 7+ for Adam.

### Filtered

**100 repos** — 100% developer/technical:

- **Language tooling (~8 repos):** coffeescript (16,579★), CoffeeScriptRedux (1,831★), js2coffee (2,081★), coffeelint (1,203★), cson (1,344★), coffeekup (1,245★), eco (1,697★), omelette (1,407★) — CoffeeScript compilers, linters, tools
- **Web animation/UI libraries (~10 repos):** mojs (18,698★), dynamics.js (7,555★), oriDomi (2,416★), sticky-kit (2,881★), jquery.shapeshift (1,654★), jquery.payment (3,509★), At.js (5,250★), bootstrap-tour (4,416★), please-wait (1,582★), jquery.turbolinks (997★) — dev libraries
- **Dev frameworks/tools (~20 repos):** chaplin (2,832★), pow (3,405★), wintersmith (3,484★), docpad (3,052★), roots (1,448★), lineman (1,168★), zappa (943★), bone.io (852★), turbolinks-classic (3,518★), stitch (1,040★), engine (2,854★), camo (1,868★), aglio (4,754★), pivottable (4,440★), cyclotron (1,544★), dispatch-proxy (3,490★), pushd (1,157★), node-rtsp-rtmp-server (1,100★), adbkit (878★), node-neo4j (924★) — infra/dev
- **Bot/automation (dev-required):** hubot-scripts (3,549★), hubot-slack (2,339★), qqbot (1,435★) — requires Hubot setup/coding
- **Browser extensions (discontinued):** SwitchyOmega (22,531★), VimFx (1,432★), vim-mode (1,711★), 4chan-x (1,119★) — browser/dev tools
- **Node.js libraries (~15 repos):** node-xml2js (4,966★), node-cache (2,375★), vibrant.js (4,597★), aurora.js (1,275★), psd.js (2,846★), kartograph.js (1,500★), xml-builder-js (926★), json-diff (1,206★), longjohn (840★), sloc (969★), node-slug (1,072★), yaml.js (887★), webgl-heatmap (915★), pt (912★), BuckyClient (1,724★) — all dev libraries
- **Misc dev tools:** morris.js (6,884★), zxcvbn (15,963★), repl.it (1,350★), Keypress (3,159★), caniuse-cmd (1,642★), octonode (1,189★), xmlbuilder-js (926★), dnschain (1,730★), dploy (969★), gulp-cheatsheet (1,371★), badges (1,207★), atom-beautify (1,503★), git-time-machine (1,111★), pretty-error (1,524★), angular-masonry (1,106★), apparatus (1,052★), shadowsocks-gui (1,997★), cloudtunes (2,503★), yakyak (3,762★) — dev/deprecated tools

---

## EvanLi Top100/Clojure.md -- 2026-05-23

### Found (7+)

- **metabase** (47,413★) — [github.com/metabase/metabase](https://github.com/metabase/metabase) — Score 7. Open-source business intelligence + analytics with a point-and-click UI (no SQL required). Self-host, connect a spreadsheet or DB, get dashboards. Adam could pipe deal pipeline data in and track conversion metrics without dev skills. Active, 47k stars.
- **logseq** (43,023★) — [github.com/logseq/logseq](https://github.com/logseq/logseq) — Score 8. Privacy-first, local-first knowledge management with bidirectional linking and graph view — essentially the open-source twin of Obsidian. Adam is already deep in Obsidian; Logseq covers the same use case with built-in task management, journals, and PDF annotation. Worth knowing as an alternative or for comparing workflows.

### Filtered

**98 repos** — Clojure Top 100 is almost entirely Clojure-language developer tooling:

- **Clojure compiler/runtime ecosystem (~12 repos):** clojurescript (9,385★), babashka (4,511★), leiningen (7,309★), boot (1,748★), shadow-cljs (2,397★), lumo (1,875★), ClojureDart (1,620★), lein-figwheel (2,877★), clj-kondo (1,840★), clojure-lsp (1,312★), cljfmt (1,216★), closh (1,628★) — all require writing Clojure code
- **UI / web frameworks (~10 repos):** re-frame (5,533★), reagent (4,869★), om (6,631★), fulcro (1,605★), electric (2,117★), pedestal (2,769★), HumbleUI (1,682★), compojure (4,113★), ring (3,876★), reitit (1,570★) — developer UI libraries
- **Databases / data engines (~8 repos):** datascript (5,761★), xtdb (2,996★), datahike (1,831★), datalevin (1,424★), honeysql (1,897★), yesql (1,497★), Korma (1,471★), carmine (1,182★) — infra/dev
- **Distributed systems / infra (~6 repos):** jepsen (7,390★), riemann (4,264★), onyx (2,051★), cascalog (1,373★), swarmpit (3,440★), maelstrom (3,592★) — infra/dev
- **Dev libraries / tooling (~40 repos):** schema (2,458★), malli (1,730★), core.async (2,047★), instaparse (2,811★), specter (2,617★), aleph (2,587★), sente (1,786★), core.logic (1,499★), clara-rules (1,231★), enlive (1,619★), hiccup (2,849★), cheshire (1,551★), clj-http (1,823★), lacinia (1,857★), plumbing (1,501★), kibit (1,758★), timbre (1,483★), Midje (1,698★), integrant (1,350★), mount (1,259★), component (2,157★), friend (1,152★), liberator (1,260★), sci (1,357★), criterium (1,225★), core.match (1,217★), core.typed (1,313★), test.check (1,147★), garden (1,362★), transit-format (1,910★), mori (3,371★), incanter (2,249★), hitchhiker-tree (1,216★), libpython-clj (1,202★), duct (1,153★), ultra (1,235★), chestnut (1,306★), drake (1,486★), seesaw (1,486★) — all dev-only
- **Learning / educational (~5 repos):** clojure-koans (3,801★), modern-cljs (2,909★), clojure-cookbook (2,616★), awesome-clojure (2,821★), cortex (1,269★, ML) — dev learning
- **Creative / niche (~4 repos):** overtone (6,183★, music programming), quil (3,046★, creative coding), Arcadia (1,685★, Clojure in Unity), dactyl-manuform (1,604★, DIY keyboard) — not wholesaling relevant
- **Borderline filtered (score 4–6):**
  - **FiraCode** (81,645★) — Programming font; dev productivity only, no wholesaling value
  - **penpot** (48,241★) — Open-source design/prototyping tool; requires design workflow, not relevant for Adam's use case
  - **athens** (6,301★) — Score 6; Roam Research clone (collaborative knowledge graph), but project is archived/unmaintained since 2023 — Logseq is the better live alternative
  - **GokuRakuJoudo** (1,396★) — Karabiner config for Mac power users; niche keyboard remapping, score 3
  - **konstellate** (1,459★) — Kubernetes GUI; infra tool, score 2
  - **clerk** (2,053★) — Clojure notebook; dev-only, score 2
  - **status-legacy** (4,013★) — Ethereum mobile OS; crypto dev, score 2
  - **code-maat** (2,590★) — Git repo mining; dev analytics, score 2

---

## EvanLi Top100/ActionScript.md -- 2026-05-23

### Found (7+)
*None.* All 100 repos score 1–3. ActionScript is Adobe Flash's language — the entire top 100 is dead-tech game engines, Flash libraries, and animation tooling. Flash reached end-of-life in December 2020; no maintained end-user applications survive in this list.

### Filtered
**100 repos** — ActionScript Top 100 is 100% Flash/game-dev infrastructure:

- **Game engines & frameworks (~25 repos):** Starling-Framework (3,053★), flixel (1,142★), Citrus-Engine (552★), FlashPunk (394★), Flashbang (205★), Ash (452★), Starling extensions ×5 — all require ActionScript/Flash to develop with; Flash runtime dead since 2020
- **Game source code / open-source games (~15 repos):** VVVVVV (7,964★, puzzle-platformer), Anodyne-1-Repo (386★), Hungry-Hero (165★), red-rogue (149★), kingdom (205★), MMORPG (246★), ElonaPlusCustom-GX (164★), glitch-client (180★) — game source dumps, not apps
- **AS3 developer libraries (~30 repos):** as3corelib (1,501★), as3-signals (1,063★), robotlegs-framework (962★), GreenSock-AS3 (422★), as3-utils (273★), flexunit (270★), BulkLoader (268★), SwiftSuspenders (278★), hamcrest-as3 (176★), mockolate (144★), promise-as3 (167★), FlashSocket.IO (210★), AS3WebSocket (251★), fzip (184★), purePDF (140★), swiz-framework (225★), flexlib (203★) — Flash developer infrastructure
- **Flash asset / export tools (~8 repos):** Fanvas (551★, Flash→HTML5 canvas), Zoe (335★, spritesheet from SWF), flump (385★, Flash animations→GPU), grapefrukt-export (198★), SWFWire (255★), as3swf (529★, SWF parser), AutoAni (170★), DragonBonesAS (250★) — Flash tooling, all obsolete
- **Media / 3D rendering engines (~8 repos):** away3d-core-fp11 (642★), Alternativa3D (382★), Papervision3D (238★), GPUImage (171★), standingwave3 (161★) — Flash 3D/GPU rendering, dead tech
- **Advocacy / petition:** open-source-flash (7,319★) — GitHub petition to open-source Flash, not a tool
- **Educational / game assets:** mapgen2 (1,367★, game map generator), glitch-avatars (213★), glitch-items (182★), books (187★, repo of book PDFs)
- **Borderline filtered (score 3–4):**
  - **boscaceoil** (594★) — music composition app built in Flash; charming but Flash-based and no longer maintained since Terry Cavanagh archived it
  - **mBlock** (329★) — Scratch-based visual programming for robotics; educational but requires Flash runtime
  - **scratch-flash** (1,358★) — Scratch 2.0 editor open-source; superseded by Scratch 3.0 (JavaScript)
  - **Spike** (321★) — CGM transmitter app for diabetics; medical niche, not RE relevant
  - **Weave** (368★) — web data visualization platform; requires dev setup
  - **ovmeet** (219★) — video conferencing platform; Flash-era, dead tech
  - **Moonshine-IDE** (136★) — IDE for ActionScript; score 3, developer tool

---

## EvanLi Top100/Haskell.md -- 2026-05-22

### Found (7+)
*None.* All 100 repos score 1–4 (Haskell programming language tooling exclusively). No standalone apps, no no-code tools, nothing useful for a non-developer.

### Filtered
**100 repos** — Entire list is Haskell-ecosystem dev infrastructure:

- **Compilers & language tools (~20):** pandoc (44,275★), shellcheck (39,471★), ghc (3,250★), purescript (8,867★), elm compiler (7,786★), ghcjs (2,618★), haste-compiler (1,482★), elm-format (1,330★), clash-compiler (1,597★) — compilers, transpilers, static analysis
- **Web frameworks & servers (~8):** postgrest (27,147★), ihp (5,286★), yesod (2,711★), scotty (1,768★), miso (2,400★), servant (1,955★), hakyll (2,854★), gitit (2,263★) — dev web tooling
- **Dev linters & formatters (~5):** hadolint (12,158★), hlint (1,594★), nixfmt (1,506★), ormolu (1,059★), shellcheck-style tools — code quality for devs
- **Academic / research / PL theory (~15):** agda (2,853★), unison (6,628★), Carp (5,915★), Kind (3,744★), Idris-dev (3,473★), liquidhaskell (1,309★), dex-lang (1,683★), futhark (2,730★), grenade (1,452★) — academic PLs and theorem provers
- **Blockchain / crypto infra (~5):** cardano-sl (3,759★), cardano-node (3,181★), plutus (1,637★), echidna (3,134★), dapptools (2,125★) — Cardano ecosystem
- **Haskell learning resources (~8):** fp-course (4,237★), awesome-haskell (3,276★), write-you-a-haskell (3,474★), wiwinwlh (2,662★), haskell-trainings (1,408★), haskell-must-watch (1,144★), course-plan (1,559★), real-world-haskell-cn (1,576★) — Haskell education
- **Window manager / desktop infra (~3):** xmonad (3,577★), kmonad (4,985★), greenclip (1,518★) — Linux power-user tools
- **Honorable mentions (scored 5–6, still filtered):** simplex-chat (11,138★, score 6) — private messenger with mobile apps but technical setup required; hledger (4,502★, score 4) — plain-text accounting CLI; taskell (1,777★, score 4) — Kanban CLI; gifcurry (1,435★, score 4) — GIF video editor

---

## EvanLi Top100/Vim-script.md -- 2026-05-22

### Found (7+)
*None.* All 100 repos score 1–2 (Vim editor plugins, config distributions, and color schemes). Vim-script's entire top 100 exists exclusively inside the text editor — zero standalone apps, zero non-technical tools.

### Filtered
**100 repos** — Every repository is either a Vim/Neovim plugin or a Vim configuration bundle:

- **Editor forks and core repos (~3):** neovim (99,793★), vim (40,379★) — the editors themselves
- **Plugin managers (~5):** vim-plug (35,663★), Vundle.vim (23,961★), vim-pathogen (12,129★), dein.vim (3,434★), neobundle.vim (2,282★) — manage Vim plugins
- **Config distributions (~10):** vimrc/amix (31,763★), SpaceVim (20,269★), spf13-vim (15,512★), janus (7,846★), macvim (7,839★), vimplus (3,950★), k-vim (4,869★), space-vim (2,852★), dotfiles/ryanb (2,380★) — opinionated Vim setups
- **File navigation/search plugins (~5):** nerdtree (20,081★), fzf.vim (10,190★), ctrlp.vim (7,239★), tagbar (6,215★), unite.vim (2,835★) — Vim-internal file navigation
- **Status bar / UI plugins (~4):** vim-airline (17,948★), lightline.vim (6,866★), vim-powerline (2,849★), vim-startify (5,399★) — Vim visual chrome
- **Color schemes (~15):** solarized (15,982★), gruvbox (15,520★), vim-colors-solarized (6,599★), molokai (3,625★), vim-colorschemes (3,460★), flatland (2,658★), onedark.vim (3,994★), everforest (4,023★), papercolor-theme (2,824★), iceberg.vim (2,364★), vim/nordtheme (2,580★), gruvbox-material (2,569★), awesome-vim-colorschemes (2,903★) — visual themes inside Vim
- **Language/syntax support plugins (~10):** vim-go (16,228★), ale (13,989★), syntastic (11,225★), vim-lsp (3,389★), copilot.vim (11,601★), windsurf.vim (5,121★), vim-javascript (3,790★), python-mode (5,470★), rust.vim (4,158★), vim-rails (4,150★), emmet-vim (6,462★) — language tooling inside Vim
- **Motion/editing plugins (~12):** vim-surround (14,070★), vim-easymotion (7,739★), vim-multiple-cursors (7,951★), vim-visual-multi (4,843★), vim-sneak (3,511★), vim-easy-align (4,237★), auto-pairs (4,199★), tabular (2,656★), vim-commentary (6,156★), vim-unimpaired (3,452★), vim-abolish (2,943★), vim-repeat (2,704★) — editing motions inside Vim
- **Dev integration / workflow plugins (~10):** vim-fugitive (21,622★), vim-gitgutter (8,497★), vimwiki (9,405★), vim-dadbod (4,376★), vimspector (4,307★), vim-test (3,154★), vim-dispatch (2,733★), neomake (2,674★), vim-autoformat (2,270★), vim-floaterm (2,650★) — dev workflow inside Vim
- **Misc editor UX (~15):** goyo.vim (4,680★, distraction-free), limelight.vim (2,446★), undotree (4,531★), vim-instant-markdown (2,753★), vim-devicons (5,809★), vim-markdown (4,802★), indentLine (4,127★), vim-polyglot (5,714★), vim-sensible (5,289★), vim-signify (2,724★), vim-indent-guides (2,656★), supertab (3,199★), editorconfig-vim (3,168★), ack.vim (3,090★), neocomplete.vim (2,727★), CoVim (2,927★, collaborative editing) — all Vim-internal
- **Reference/guides:** vim-galore (17,849★), vim-galore-zh_cn (10,642★), use_vim_as_ide (9,179★), til (14,094★, dev TIL — not a tool)
- **Misc infra:** vim.wasm (5,625★, Vim in browser — novelty), codi.vim (3,058★, interactive scratchpad — dev only), vimux (2,274★, Vim+tmux bridge — dev only), vim-table-mode (2,236★, table creation in Vim — dev only)

---

## EvanLi Top100/Top-100-forks.md -- 2026-05-22

### Found (7+)
- **ChatGPTNextWeb/NextChat** (88,065★) — Cross-platform AI chat assistant UI (Web, iOS, macOS, Android). Plug in any provider key (Claude, GPT-4, Gemini, DeepSeek) and get a clean, fast chat interface — no code needed. Hosted version at app.nextchat.dev requires zero setup; self-host via Vercel one-click if Adam ever wants his own. Beats browser tabs for AI work — persistent config, multiple conversations, custom system prompts baked in. Score 8.
- **asgeirtj/system-prompts-and-models-of-ai-tools** (138,035★) — Collected and reverse-engineered system prompts from ChatGPT, Claude, Copilot, Grok, Gemini, Perplexity, and more. Not a runnable app but a reference vault: Adam can study how production AI tools are instructed and steal patterns for his own CLAUDE.md, skills, and agent prompts. For a Claude Code Agentic OS power user, this is the highest-leverage reading material. Score 7.

### Filtered
**98 repos** — Top-100-forks is dominated by:
- **Course materials and coding exercises (~20 repos):** datasharing, ProgrammingAssignment2, ExData_Plotting1, RepData_PeerAssessment1, css-exercises, javascript-exercises, it-cert-automation-practice, JavaScript30, jbbmo-Introduction-to-Git-and-GitHub, patchwork, spring-petclinic, courses, simple-java-maven-app, mslearn-tailspin-spacegame-web, DO180-apps, dotfiles, swot — all tutorial/homework repos
- **Educational mega-lists (~8 repos):** free-programming-books (388,698★), coding-interview-university (347,203★), developer-roadmap (355,217★), system-design-primer (349,742★), project-based-learning (266,318★), build-your-own-x (503,058★), JavaGuide (155,814★), free-programming-books-zh_CN (116,979★) — reference lists for programmers, not tools
- **Web/app frameworks (~18 repos):** react, vue, angular, angular.js, next.js, bootstrap, flutter, ant-design, material-ui, spring-boot, spring-framework, django, three.js, node, create-react-app, pytorch, scikit-learn, transformers — developer infrastructure
- **Language tooling and infra (~8 repos):** linux (kernel), cpython, git, kubernetes, vscode, github-readme-stats, gitignore, qmk_firmware, DefinitelyTyped
- **Learning/style resources:** CS-Notes, Python-100-Days, Python (algorithms), javascript-algorithms, javascript (Airbnb style guide), You-Dont-Know-JS, Java-design-patterns, learning-area, awesome-python
- **Borderline filtered (score 5–6):**
  - **AutoGPT** (184,445★) — Autonomous AI agent platform. Vision is right but setup requires Python, Docker, and API key plumbing. Non-technical overhead too high vs. tools already found. Score 5.
  - **stable-diffusion-webui** (163,206★) — AI image generation UI. Potentially useful for real estate marketing visuals but requires NVIDIA GPU + Python install. Cloud alternatives exist but this repo is self-host only. Score 6.
  - **daily_stock_analysis** (38,351★) — LLM-powered stock market analysis. Finance-adjacent but focused on equity markets, not real estate. Score 5.
  - **Home Assistant core** (87,179★) — Smart home automation with local control. Not relevant to wholesaling workflow. Score 5.
- **Already in findings:** odoo (found Python batch)
- **Skip list hits:** openclaw, n8n
- **Synthetic/suspicious repos flagged:**
  - **claw-code** (192,186★) — Description "The fastest repo in history to surpass 100K stars" is a marketing claim, not a product description. Likely synthetic star-farming repo (same pattern as openclaw). Filtered.
  - **ECC** (188,227★) — "Agent harness performance optimization system" — vague name, no real project found at this description. Suspicious star count. Filtered.
  - **Spoon-Knife, patchwork, websites, dio-lab-open-source** — demo/training repos with inflated forks from GitHub Education programs; not real projects.

---

## EvanLi Top100/R.md -- 2026-05-22

### Found (7+)
*None.* All 100 repos score 1–3 (statistical computing / data science / bioinformatics). R's Top 100 is exclusively statistical packages, visualization libraries, and academic course materials — zero standalone apps for non-technical users.

### Filtered
**100 repos** — R is a statistical computing language; the entire top 100 is R packages, academic tutorials, and ML/bioinformatics research tools:

- **Core R packages and data manipulation (~30 repos):** ggplot2 (6,932★), dplyr (5,025★), data.table (3,890★), tidyverse (1,791★), tidyr (1,429★), purrr (1,391★), ggstatsplot (2,182★), ggthemes (1,355★), ggrepel (1,256★), ggpubr (1,242★), ggraph (1,115★), ggforce (951★), gganimate (1,982★), gt (2,148★), broom (1,515★), janitor (1,446★), readr (1,032★), magrittr (970★), httr (982★), renv (1,148★), lintr (1,276★), box (964★), wesanderson (2,109★), patchwork (2,604★), bbplot (1,629★), hrbrthemes (1,344★), r-color-palettes (1,694★), MetBrewer (1,256★), paletteer (1,037★), see (946★) — all require R installation and programming knowledge
- **ML and statistical inference packages (~20 repos):** caret (1,674★), mlr (1,680★), mlr3 (1,066★), brms (1,405★), rstan (1,078★), CausalImpact (1,830★), AnomalyDetection (3,609★), forecast (1,168★), easystats (1,153★), performance (1,141★), gtsummary (1,188★), clusterProfiler (1,204★), seurat (2,730★, single-cell genomics), benchm-ml (1,895★), rmarkdown (3,038★), knitr (2,452★), drake (1,342★), targets (1,077★), future (1,012★), sparklyr (969★, Spark interface) — all statistical/ML developer tools
- **Academic course materials and textbooks (~15 repos):** stat_rethinking_2022/2023/2024 (4,104★/2,377★/1,788★), r4ds (5,055★), rethinking (2,382★), stats337 (1,614★), DataScienceR (2,132★), ML_for_Hackers (3,739★), statistics-for-data-scientists (1,222★), swirl_courses (4,550★, interactive R learning), swirl (1,212★), fasteR (1,146★), R/TheAlgorithms (1,143★), r-pkgs (944★, how to build R packages), labs (2,143★, HarvardX genomics) — all require R and statistics knowledge
- **Bioinformatics / specialist science (~10 repos):** seurat (2,730★, single-cell RNA), clusterProfiler (1,204★, omics), ComplexHeatmap (1,496★), circlize (1,015★, circular viz), rnaseq_tutorial (1,422★), tofsims (1,495★, radiation analysis), MoRad (965★, radiation analysis), brms (1,405★, Bayesian), rstan (1,078★, Stan interface), rayshader (2,160★, 3D mapping in R) — highly specialist academic tools
- **R developer tooling and infra:** devtools (2,509★), r-source (1,231★, R mirror), rstan, reticulate (1,748★, Python-R bridge), plumber (1,436★, R API server), shiny (5,651★, R web apps), advanced-shiny (1,218★), awesome-shiny-extensions (1,654★), mastering-shiny (1,378★), blogdown (1,788★, R website generator), vitae (1,268★, R Markdown CV generator), tinytex (1,122★, LaTeX in R), gptstudio (989★, GPT addins for RStudio), golem (939★, Shiny app framework) — all require R developer context
- **Curated resource lists (R-specific, not tools):** awesome-R (6,460★), awesome-network-analysis (4,044★), r-color-palettes (1,694★), FriendsDontLetFriends (7,060★, data viz do's/don'ts guide) — reference lists for data professionals
- **Data and course datasets:** palmerpenguins (1,008★, penguin dataset), nyc-taxi-data (2,071★, PostgreSQL/ClickHouse import scripts), geocompr (1,765★, R geocomputation book), investing (1,747★, market return charts in R), esquisse (1,849★, RStudio ggplot2 builder add-in), DiagrammeR (1,735★, network graphs in R), pointblank (1,033★, R data quality) — all require R to use
- **Borderline filtered (score 3–4):**
  - **vitae** (1,268★) — generates résumés from R Markdown. Score 3. Non-technical output but requires RStudio to author; LaTeX + R dependency chain is too heavy
  - **investing** (1,747★) — market return visualizations from public data. Score 2. The charts exist as static images but tool itself requires R to regenerate
  - **gptstudio** (989★) — GPT addins for RStudio. Score 3. AI integration but RStudio-only and R knowledge required; cherry-studio already found handles AI chat far better

---

## EvanLi Top100/MATLAB.md -- 2026-05-21

### Found (7+)
*None.* All 100 repos score 1–3 (ML research / academic code). MATLAB's Top 100 is exclusively academic and research-grade software.

### Filtered
**100 repos** — MATLAB is a scientific computing language; the top 100 is 100% ML research, computer vision, signal processing, robotics, and course assignments. Not a single end-user application exists in the list:

- **ML/computer vision research papers with code (~55 repos):** deep-photo-styletransfer (9,998★), OpenFace (7,654★), PRMLT (6,204★), vrn (4,519★), DeepLearnToolbox (3,871★), MTCNN_face_detection_alignment (2,865★), faster_rcnn (2,830★), rcnn (2,415★), PlatEMO (2,102★), OpenTLD (2,100★), CAM (1,886★), DnCNN (1,708★), crfasrnn (1,337★), R-FCN (1,248★), Image-Fusion (1,189★), tiny (1,144★), convnet-burden (929★), lrslibrary (884★), NTURGB-D (871★), VAD (870★), toolbox (859★), edges (838★), hctsa (827★), Awesome-Speech-Enhancement (825★), Image-Harmonization-Dataset-iHarmony4 (808★), activityrecognition (930★), MatlabFunc (625★), ECO (624★), IRCNN (612★), ICNet (609★), refinenet (603★), netvlad (601★), SelfExSR (636★), cnn-for-image-retrieval (632★), hashing-baseline-for-image-retrieval (630★), siamese-fc (628★), Exclusively-Dark-Image-Dataset (628★), face_verification_experiment (721★), vgg_face2 (704★), Detect-Track (552★), Exposure_Correction (583★), voc-dpm (577★), FFDNet (556★) — all academic paper code, requires MATLAB and ML knowledge
- **Robotics / control / navigation (~13 repos):** robotics-toolbox-matlab (1,525★), quadrotor (1,110★), Gait-Tracking-With-x-IMU (1,062★), MATLABRobotics (676★), OptimTraj (705★), automated-driving-control (679★), automatic-driving-decision-and-planning-for-matlab (618★), matlab_motion_planning (627★), robust-tube-mpc (596★), MSS (677★), NaveGo (632★), kalibr_allan (659★), IMUCalibration-Gesture (787★) — specialist robotics/control research
- **ML course assignments (~11 repos):** Stanford-CS-229 (3,451★), Machine-Learning-homework (2,020★), Algorithms_MathModels (2,338★), MCM-ICM (2,268★), Math_Model (4,484★), Coursera-Machine-Learning-Stanford (1,154★), machine-learning-coursera-1 (1,118★), Octave (834★), machine-learning-octave (893★), CourseraMachineLearning (778★), Notes-ML-AndrewNg (560★) — student coursework only
- **Specialist academic toolboxes (~22 repos):** Book-Mathematical-Foundation-of-Reinforcement-Learning (16,242★), fieldtrip (965★), eeglab (764★), TIGRE (773★), MIMO_OFDM (972★), Must-Reading-on-ISAC (914★), SAR-Synthetic-Aperture-Radar (1,018★), Signals-and-Systems-course (1,004★), gptoolbox (670★), chebfun (667★), mexopencv (659★), matpower (559★), YALMIP (556★), MATLAB-Deep-Learning-Model-Hub (559★), BPL (982★), omniglot (1,418★), export_fig (1,343★), matlab-schemer (1,255★), matlab2tikz (1,712★), awesome-time-series-segmentation-papers (548★), awesome-matlab-students (656★), awesome-low-light-image-enhancement (1,818★) — require MATLAB licence + domain expertise
- **Misc/non-relevant:** eviltransform (2,565★, GPS coordinate transform), EconometricsResources (1,064★, economics references), Mathematics (746★, math notes), Coding-Guide (1,456★, personal coding notes), SPIRIT (1,179★, Raspberry Pi smartphone project), BeatTheBookie (646★, football betting analysis), Smart-Algorithm (836★, optimisation algorithm code), CBIG (742★, brain imaging research)

---

## EvanLi Top100/PowerShell.md -- 2026-05-21

### Found (7+)
- **YerongAI/Office-Tool** (13,476★) — GUI app for deploying, configuring, and managing Microsoft Office installs on Windows. Click to install any Office version/channel, switch between 365/2021/LTSC, remove bloat apps, activate — no PowerShell knowledge needed, no command line. One tool to manage every Office install on any Windows machine Adam sets up. Score 7.

### Filtered
**99 repos** — PowerShell Top 100 is the worst batch of this research run for Adam:

- **Security/pentesting (~45 repos):** PowerSploit (13k★), BloodHound-Legacy (10.5k★), nishang (9.9k★), Empire (7.8k★), GOAD (7.8k★), commando-vm (7.6k★), Flipper-Zero-BadUSB (6.8k★), K8tools (6.2k★), usbrubberducky-payloads (5.7k★), flare-vm (8.7k★), RedTeaming-Tactics-and-Techniques (4.6k★), Invoke-Obfuscation (4.3k★), PrivescCheck (3.8k★), OSCP (3.7k★), WinPwn (3.7k★), MailSniper (3.2k★), sysmon-modular (3k★), Penetration-Testing-Tools (2.9k★), bashbunny-payloads (2.9k★), PowerShell-Suite (2.7k★), PowerUpSQL (2.7k★), Active-Directory-Exploitation-Cheat-Sheet (2.7k★), windows_hardening (2.6k★), ScubaGear (2.6k★), sRDI (2.5k★), AzureAD-Attack-Defense (2.5k★), DeepBlueCLI (2.4k★), MicroBurst (2.4k★), powercat (2.4k★), vulnerable-AD (2.3k★), BadBlood (2.2k★), PowerTools (2.2k★), Invoke-PSImage (2.2k★), PersistenceSniper (2.1k★), PoshC2 (2.1k★), UltimateAppLockerByPassList (2.1k★), DomainPasswordSpray (2.1k★), mimikittenz (1.9k★), badusb (1.9k★), Sherlock (2k★), JAWS (1.9k★), HardeningKitty (1.8k★) — all offensive/defensive security, zero relevance
- **Developer tools/frameworks:** core/dotnet (22k★), blazor (9.3k★), machinelearning-samples (4.7k★), cmder (26.9k★), Scoop (24k★), posh-git (8.2k★), docker/jenkins (7.5k★), k8s-for-docker-desktop (5.1k★), awesome-powershell (5.4k★), oh-my-posh2 (5.2k★), Pester (3.3k★), Terminal-Icons (2.9k★), PowerShell-Docs (2.5k★), PSKoans (1.9k★), dbatools (2.8k★), chocolatey (2.8k★), psmux (2.1k★), winfetch (1.8k★), windows-dev-box-setup-scripts (1.9k★), Fast-Kubernetes (3.3k★), awesome-love2d (4.4k★), ScoopInstaller/Main (1.8k★), ScoopInstaller/Extras (2.1k★) — all developer infra
- **Windows sysadmin/IT:** runner-images (12.8k★), AutomatedLab (2.2k★), IntuneManagement (2k★), Microsoft365DSC (2.3k★), Enterprise-Scale (1.9k★), Virtualization-Documentation (1.9k★), Microsoft-Defender-for-Cloud (1.9k★), MicrosoftDocs/PowerShell-Docs (2.5k★), powershell-scripts/O365 (1.9k★), lazywinadmin/PowerShell (2.9k★) — IT admin tooling, not end-user
- **Borderline filtered (score 5–6):**
  - **ChrisTitusTech/winutil** (54,794★) — GUI Windows tweaker/installer. Score 6. Useful for PC setup but one-time; doesn't add to Adam's daily workflow
  - **Raphire/Win11Debloat** (46,498★) / **Sycnex/Windows10Debloater** (18.8k★) / **W4RH4WK/Debloat-Windows-10** (6.2k★) / **LeDragoX/Win-Debloat-Tools** (6.4k★) — Windows cleanup scripts. Score 5. One-time utility
  - **SpotX-Official/SpotX** (21k★) — Spotify ad patcher. Score 5. Entertainment, not work
  - **ntdevlabs/tiny11builder** (18.7k★) — Build trimmed Windows ISO. Score 4. Requires reinstall
  - **ThioJoe/Windows-Super-God-Mode** (2k★) — Windows settings shortcuts. Score 6. Interesting for power users
  - **Romanitho/Winget-AutoUpdate** (1.9k★) — Auto-update Windows apps. Score 6. Good system hygiene, not a workflow tool
  - **EmpireMediaScience/A1111-Web-UI-Installer** (1.8k★) — Stable Diffusion installer. Score 4. Requires Nvidia GPU
  - **GuDaStudio/skills** (2k★) — Claude AI agent skills. Score 9 but already found in Shell batch

---

## EvanLi Top100/Dart.md -- 2026-05-21

### Found (7+)
- **localsend/localsend** (81,664★) — Cross-platform local file sharing with no internet, no cloud, no account — AirDrop-equivalent for any OS combination. Install on phone + laptop, share deal docs, contracts, and property photos instantly over local WiFi. Score 7.
- **ente-io/ente** (26,549★) — End-to-end encrypted photo and file storage (Google Photos/iCloud replacement). Mobile + desktop apps, SaaS cloud included, no server to run. All property walkthrough photos stay private and backed up with no Big Tech access. Score 7.

### Filtered
**98 repos** — Dart is Flutter's language; top 100 is almost entirely Flutter framework tooling, developer libraries, mobile UI templates, and entertainment apps:

- **Framework/SDK/language:** flutter (176k★), dart-lang/sdk (11k★), awesome-flutter (60k★), flutter/samples (19k★), flutter/plugins (17k★), flutter/gallery (6k★), flutter/packages (5k★) — core dev infrastructure
- **Dev libraries/state management/routing:** felangel/bloc (12k★), jonataslaw/getx (11k★), rrousselGit/riverpod (7k★), rrousselGit/provider (5k★), firebase/flutterfire (9k★), cfug/dio (12k★), isar/hive (4k★), isar/isar (4k★), flame-engine/flame (10k★), imaNNeo/fl_chart (7k★), alibaba/fish-redux (7k★), alibaba/flutter_boost (7k★), OpenFlutter/flutter_screenutil (4k★), xuelongqy/flutter_easy_refresh (4k★), pichillilorenzo/flutter_inappwebview (3k★), lukepighetti/fluro (3k★), best-flutter/flutter_swiper (3k★), ReactiveX/rxdart (3k★), bdlukaa/fluent_ui (3k★), fzyzcjy/flutter_rust_bridge (5k★), sass/dart-sass (4k★) — developer-only libraries
- **Dev learning/examples/templates:** Solido/awesome-flutter (60k★), alibaba/flutter-go (23k★), mitesh77/Best-Flutter-UI-Templates (22k★), iampawan/FlutterExampleApps (21k★), brianegan/flutter_architecture_samples (8k★), toly1994328/FlutterUnit (8k★), simplezhli/flutter_deer (8k★), nisrulz/flutter-examples (7k★), abuanwar072/Flutter-Responsive-Admin-Panel-or-Dashboard (7k★), vandadnp/flutter-tips-and-tricks (6k★), 2d-inc/HistoryOfEverything (6k★), iampawan/Flutter-UI-Kit (6k★), samarthagarwal/FlutterScreens (6k★), flutterchina/flukit (5k★), AweiLoveAndroid/Flutter-learning (5k★), Sky24n/flutter_wanandroid (5k★), OpenFlutter/Flutter-Notebook (7k★), FilledStacks/flutter-tutorials (4k★), lohanidamodar/flutter_ui_challenges (4k★), FlutterOpen/flutter-ui-nice (3k★), gskinnerTeam/flutter_vignettes (4k★), gskinnerTeam/flutter-folio (3k★), gskinnerTeam/flutter-wonderous-app (4k★), tortuvshin/open-source-flutter-apps (4k★), TheAlphamerc/flutter_twitter_clone (4k★), TheAlphamerc/flutter_ecommerce_app (3k★), LianjiaTech/bruno (3k★), roughike/inKino (3k★), abuanwar072/E-commerce-Complete-Flutter-UI (4k★), leoafarias/fvm (5k★), kaina404/FlutterDouBan (9k★), CarGuo/gsy_github_app_flutter (15k★) — all developer learning
- **VPN/proxy/circumvention:** chen08209/FlClash (39k★), hiddify/hiddify-app (29k★), getlantern/lantern (15k★), KaringX/karing (11k★), KaringX/clashmi (7k★) — technical networking setup required
- **Entertainment (video/music/manga/anime):** KRTirtho/spotube (46k★), Predidit/Kazumi (25k★), xiaoyaocz/dart_simple_live (15k★), bggRGjQaUbCoE/PiliPlus (14k★), guozhigq/pilipala (13k★), Notsfsssf/pixez-flutter (11k★), venera-app/venera (9k★), wgh136/PicaComic (8k★), ComicSparks/pikapika (8k★), ComicSparks/jasmine (5k★), jiangtian616/JHenTai (5k★), Sle2p/AniCh (4k★), namidaco/namida (5k★), miru-project/miru-app (5k★), harmonoid/harmonoid (4k★), gokadzev/Musify (3k★), UnicornsOnLSD/finamp (3k★), spotiflacapp/SpotiFLAC-Mobile (4k★) — entertainment only, not work
- **Dev tools/infra:** wanghongenpin/proxypin (13k★, HTTP traffic capture), lollipopkit/flutter_server_box (7k★, server monitoring), bostrot/wsl2-distro-manager (3k★, WSL GUI), alesimula/wsa_pacman (4k★, WSA package manager) — technical
- **Borderline filtered (score 5–6):**
  - **AppFlowy-IO/AppFlowy** (70k★) — Notion alternative with AI; AFFiNE already found (68k★, TypeScript batch) covers same territory
  - **Anxcye/anx-reader** (8k★) — E-book reader with AI; niche, not RE-specific
  - **saber-notes/saber** (4k★) — Cross-platform handwriting notes; Adam has Obsidian
  - **jameskokoska/Cashew** (4k★) — Mobile budget tracker; firefly-iii + maybe-finance already found
  - **GitJournal/GitJournal** (4k★) — Git-backed mobile notes; Obsidian already covers notes
  - **ImranR98/Obtainium** (17k★) — Android APK updates from GitHub; needs APK sideloading knowledge
  - **BasedHardware/omi** (12k★) — AI screen observer; unclear if standalone app or requires hardware device
  - **mylxsw/aidea** (6k★) — Multi-model AI app; cherry-studio (45k★) already found, more established
  - **TheLastGimbus/GooglePhotosTakeoutHelper** (5k★) — One-time migration utility; limited ongoing value
  - **bagisto/opensource-ecommerce-mobile-app** (15k★) — E-commerce; not RE wholesale relevant
  - **deckerst/aves** (4k★) — Android gallery + metadata viewer; narrow scope

---

## EvanLi Top100/Top-100-stars.md -- 2026-05-21

### Found (7+)
- **awesome-selfhosted/awesome-selfhosted** (294,154★) — The definitive curated index of 2,000+ self-hosted open-source apps organised by category (automation, CRM, email, file management, notes, finance, etc.). Not a tool itself but the highest-signal discovery resource in this entire research run — every future tool gap Adam has is answered here before he Googles. Permanent reference. Score 7.

### Filtered
**99 repos** across the entire top-100-by-stars list:

- **Skip list hits (already catalogued):** openclaw (373k★), n8n (188k★), markitdown (124k★)
- **Already found in prior batches:** open-webui (138k★, Python), prompts.chat (162k★, HTML), PowerToys (133k★, CSharp), rustdesk (114k★, Rust), anthropics/skills → "skills" (Shell)
- **Previously evaluated and filtered (not new):** AutoGPT (184k★, Python coding required), langflow (148k★, score 5–6 Docker, Python batch), ollama (171k★, score 5–6 CLI, Go batch), dify (142k★, score 6 Docker, TypeScript batch), excalidraw (123k★, score 5–6 whiteboard SDK, TypeScript batch), awesome-mac (104k★, score 5–6 list not tool, Swift batch), gemini-cli (104k★, terminal agent, TypeScript batch)
- **⚠️ Synthetic/suspicious entries (star counts implausible vs repo age/description):** obra/superpowers (200k★) — "Agentic skills framework for development"; ultraworkers/claw-code (192k★) — "Fast-growing Rust repository"; affaan-m/ECC (187k★) — "Agent harness performance optimization system"; anomalyco/opencode (163k★) — "Open source coding agent"; NousResearch/hermes-agent (159k★) — "The agent that grows with you"; multica-ai/andrej-karpathy-skills (141k★) — "Claude Code behavior improvement file"; github/spec-kit (104k★) — "Spec-Driven Development toolkit." All flagged: known real organisations used as cover accounts or description phrasing identical to synthetic patterns seen in prior batches.
- **Score 5–6 close misses:** AUTOMATIC1111/stable-diffusion-webui (163k★) — AI image gen but requires Nvidia GPU + Python env; scrcpy (142k★) — Android screen control, needs ADB setup; firecrawl (122k★) — web scraping API, dev-first; ComfyUI (113k★) — node-based diffusion editor, even more technical than SD-webui; x1xhlol/system-prompts-and-models-of-ai-tools (137k★) — AI prompts collection, interesting but passive reference; FreeDomain (163k★) — free domain registration, not relevant to current phase; iptv-org/iptv (116k★) — entertainment only; massgravel/Microsoft-Activation-Scripts (175k★) — Windows/Office activation, sketchy territory
- **Dev/infra/education (score 1–4, ~75 repos):** build-your-own-x (502k★), freeCodeCamp (445k★), public-apis (436k★), free-programming-books (388k★), developer-roadmap (355k★), system-design-primer (349k★), coding-interview-university (347k★), awesome-python (298k★), project-based-learning (266k★), react (245k★), linux (233k★), the-book-of-secret-knowledge (221k★), TheAlgorithms/Python (221k★), vue (209k★), ossu/computer-science (204k★), javascript-algorithms (195k★), tensorflow (195k★), ohmyzsh (187k★), vscode (185k★), You-Dont-Know-JS (184k★), CS-Notes (184k★), Python-100-Days (182k★), flutter (176k★), bootstrap (174k★), gitignore (174k★), awesome-go (173k★), yt-dlp (163k★), the-art-of-command-line (161k★), transformers (160k★), JavaGuide (155k★), airbnb/javascript (148k★), youtube-dl (140k★), tech-interview-handbook (139k★), next.js (139k★), langchain (137k★), golang/go (133k★), fucking-algorithm (133k★), 30-seconds-of-code (127k★), hello-algo (126k★), react-native (125k★), claude-code (125k★), d3 (112k★), Awesome-Hacking (112k★), three.js (112k★), llama.cpp (111k★), awesome-llm-apps (111k★), generative-ai-for-beginners (111k★), godot (110k★), axios (109k★), TypeScript (108k★), GrowingGit/GitHub-Chinese-Top-Charts (108k★), tauri (106k★), deno (106k★), frp (106k★), papers-we-love (106k★), 2dust/v2rayN (106k★), nodebestpractices (105k★), deepseek-ai/DeepSeek-V3 (103k★), clash-verge-rev (119k★), nodejs/node (117k★), free-programming-books-zh_CN (116k★), shadcn-ui/ui (114k★), rust-lang/rust (112k★), 996icu (276k★), electron (121k★), kubernetes (122k★)

---

## EvanLi Top100/CSharp.md -- 2026-05-21

### Found (7+)
- **microsoft/PowerToys** (133,340★) — Microsoft's official Windows productivity megapack: FancyZones window snapping layouts, PowerRename bulk file rename with regex, Text Extractor (on-screen OCR to clipboard), Peek spacebar file preview, Keyboard Manager, Color Picker, File Locksmith. Single Microsoft-signed installer, zero config. Entire Windows workflow upgrades in one install. Score 9.
- **ShareX/ShareX** (37,621★) — Full-featured Windows screen capture, annotation, and recording. Capture regions/windows/fullscreen, annotate with arrows/text/blurs, upload to cloud/Imgur/S3, create video recordings. Essential for documenting deal walkthroughs, seller call summaries, and SOP visuals. Windows counterpart to QuickRecorder already found (macOS). Score 8.
- **NickeManarin/ScreenToGif** (26,964★) — Record any screen region directly as an optimized GIF with a frame-level editor. Non-technical, point-and-click. Create quick visual demos for sellers (how to sign DocuSign), document deal steps, export property walkthrough clips. Score 7.
- **QL-Win/QuickLook** (23,467★) — Brings macOS-style spacebar file preview to Windows. Tap space on any PDF, image, video, Word doc, or spreadsheet to preview without opening the app. Fast contract skimming and property photo review without an app launch. Score 7.
- **Klocman/Bulk-Crap-Uninstaller** (19,226★) — Bulk app removal for Windows with deep uninstall (leftover files, registry keys). GUI-only, no terminal. One pass clears Windows bloat so agentic sessions run on a clean, fast system. Score 7.
- **duplicati/duplicati** (14,557★) — Encrypted automated backup to any cloud (OneDrive, Google Drive, S3, Backblaze). GUI setup wizard, scheduled backups, no server. Protects Obsidian vault, deal docs, and contract archives from data loss. Nothing else in the found stack covers backup. Score 7.
- **Tichau/FileConverter** (14,405★) — Right-click context menu file converter for Windows: images (HEIC→JPG, PNG→PDF), audio (M4A→MP3), video (MOV→MP4), documents. Zero extra workflow — right-click the file, pick output format, done. Converts seller iPhone photos, voice memos, and property clips without any app launch. Score 7.

### Filtered
**~93 repos** — C# is a Microsoft-stack language; top 100 is dominated by .NET frameworks, dev tools, gaming, and Windows power-user utilities:

- **VPN/proxy clients:** v2rayN (106k★), shadowsocks-windows (59k★), netch (17k★) — technical networking setup required
- **Dev frameworks, runtimes, compilers:** PowerShell (53k★), aspnetcore (37k★), dotnet/maui (23k★), dotnet/runtime (17k★), Avalonia (30k★), roslyn (20k★), efcore (14k★), MonoGame (13k★), orleans (10k★), csharplang (12k★), abp (14k★), aspnetboilerplate (11k★), mono (11k★), cefsharp (10k★), BenchmarkDotNet (11k★) — all developer tooling
- **Dev libraries (never touch):** Dapper (18k★), Polly (14k★), QuestPDF (14k★), spectre.console (11k★), Newtonsoft.Json (11k★), Terminal.Gui (10k★), MediatR (11k★, note: listed under LuckyPennySoftware — likely EvanLi scraper attribution error; real repo is jbogard/MediatR), AutoMapper (10k★, same attribution oddity), MudBlazor (10k★) — .NET libraries, require coding
- **Dev tools, docs, architecture references:** dnSpy (29k★), ILSpy (25k★), PEASS-ng (19k★, privilege escalation toolkit), Dependencies (11k★), winsw (13k★), AspNetCore.Docs (13k★), eShopOnContainers (24k★), eShopOnWeb (10k★), eShop (10k★), Clean Architecture templates ×2 (20k★+18k★), modular-monolith-with-ddd (13k★), awesome-dotnet-core (21k★), DotNetGuide (10k★), practical-aspnetcore (10k★), coding-horror/basic-computer-games (11k★) — developer reference only
- **Gaming / entertainment apps:** SteamTools (25k★), osu (18k★), OpenRA (16k★), better-genshin-impact (13k★), ArchiSteamFarm (13k★), Playnite (13k★) — gaming, not work
- **ML / game dev toolkits:** Unity-Technologies/ml-agents (19k★), WaveFunctionCollapse (25k★), UnityCsReference (12k★), Cysharp/UniTask (10k★) — game engine / ML dev
- **Media download CLI tools:** N_m3u8DL-CLI (15k★, HLS/DASH CLI), BBDown (13k★, Bilibili CLI) — CLI-only; Motrix/Seal/lux already found
- **Torrent/arr automation:** Jackett (15k★), Sonarr (13k★), Radarr (13k★) — technical media automation
- **Windows activation tools:** CMWTAT_Digital_Edition (19k★), LKY_OfficeTools (11k★) — sketchy licensing territory, not work tools
- **China-specific / irrelevant:** huiyadanli/RevokeMsgPatcher (37k★, WeChat/QQ patcher), xupefei/Locale-Emulator (11k★, regional simulation)
- **Password server (already covered):** bitwarden/server (18k★) — server-side component, KeePassXC already found for client use
- **Cosmetic / entertainment:** rocksdanister/lively (18k★, animated wallpapers), CodeHub iOS (22k★, GitHub iOS client for devs)
- **Borderline filtered (score 5–6):**
  - DevToys (31k★) — dev utilities collection, Adam not the audience
  - UniGetUI (23k★) — GUI over package managers, still requires package management knowledge
  - Flow.Launcher (14k★) — quick launcher for Windows; Wox (26k★) already found, same category
  - Tyrrrz/YoutubeDownloader (15k★) — Windows YouTube GUI; Motrix+Seal+lux already cover downloads
  - hellzerg/optimizer (18k★) + Winhance (10k★) — Windows system optimizers; PowerToys already qualifies as primary Windows utility; both are one-time cleaners, low ongoing value
  - EverythingToolbar (14k★) — requires Everything search to be pre-installed; extra dependency layer
  - ContextMenuManager (19k★) — cleans Windows right-click menu; power-user config, minor payoff
  - DiscordChatExporter (11k★) — useful but not RE relevant
  - EarTrumpet (11k★) — advanced volume control; minor quality-of-life
  - ImageGlass (13k★) — image viewer; upscayl (already found) is more impactful
  - Kavita (10k★) — reading server; not work-relevant
  - mRemoteNG (10k★) — multi-protocol remote manager; RustDesk already found
  - Notepads (10k★) — minimal text editor; marktext already found
  - SubtitleEdit (12k★) — subtitle editor; niche
  - PDFPatcher (12k★) — PDF bookmark/page editor; Stirling-PDF already found and more capable
  - chocolatey/choco (11k★) — Windows package manager CLI; technical, score 4
  - Captura (10k★) — screen capture; ShareX already found; Captura appears archived/unmaintained
- **⚠️ Suspicious entry:** MiniMax-AI/skills (11,985★) — no description provided in EvanLi data. MiniMax is a real Chinese AI company but this repo pattern (account/skills, ~12k stars, no description) matches the synthetic Claude skills repo signature seen in TypeScript and Shell batches. Cannot verify; excluded from count.

---

## EvanLi Top100/HTML.md -- 2026-05-20

### Found (7+)
- **prompts.chat** (162,543★) — Community library for discovering and sharing AI prompts. Adam delegates heavily to Claude; a searchable prompt bank shortens the gap between "what I want" and "what I type." Score 7.
- **PakePlus** (12,346★) — Wraps any web app into a native desktop/mobile app with no coding (Tauri-based, GUI workflow). If Adam wants a specific tool always one click away as a standalone app, this does it without any terminal work. Score 7.

### Flagged Synthetic (descriptions too on-point, star counts don't match repo history)
- **claude-code-best-practice** (53,892★) — shanraisshan — "Best practices guide for agentic engineering with Claude." 53k stars on a niche Claude guide is implausible; description is too perfectly tailored. Flagged, do not use.
- **huashu-design** (14,354★) — alchaincyf — "HTML-native design skillset for Claude Code agents." alchaincyf is a real creator but this description reads as LLM-fabricated for this scan. Flagged.
- **guizang-ppt-skill** (10,396★) — op7418 — "AI agent skill for generating HTML slide presentations." Description format mimics Claude Code skill naming but repo identity unverifiable. Flagged.

### Filtered
**95 repos** — 100% dev/infra/education:
- **CS/dev education (huge repos):** computer-science (204k★), cs-self-learning (72k★), Coursera-ML-AndrewNg-Notes (36k★), deeplearning_ai_books (20k★), JavaScript30 (29k★), en.javascript.info (25k★), zh.javascript.info (10k★), llm-action (24k★), llm_interview_note (14k★), ai-edu (14k★), Modern-CPP-Programming (15k★), awesome-modern-cpp (13k★), flash-linux0.11-talk (22k★), blog_os (17k★), nndl.github.io (18k★), craftinginterpreters (10k★), machine-learning-systems-design (10k★), raytracing.github.io (10k★), deep-learning-drizzle (12k★) — pure learning/dev
- **Front-end frameworks/libs:** alpine (31k★), foundation-sites (29k★), material-design-lite (32k★), polymer (22k★), uikit (18k★), zepto (15k★), fastclick (18k★), skrollr (18k★), rough (20k★), masonry (16k★), isotope (11k★), You-Dont-Need-JavaScript (20k★), galaxy (10k★), hyperui (12k★) — dev UI tooling
- **Dashboard/admin templates:** tabler (41k★), gentelella (21k★), coreui-free-bootstrap-admin-template (12k★), dashboards (11k★), design-blocks (13k★) — require dev setup
- **Dev resources/curated lists:** free-for-dev (122k★), hacker-laws (27k★), awesome-generative-ai-guide (26k★), Awesome-Linux-Software (24k★), skill-map (21k★), architecture.of.internet-product (20k★), awesome-creative-coding (14k★), Awesome-Diffusion-Models (12k★), awesome-piracy (26k★), awesome-quant (26k★), deep-learning-drizzle (12k★) — developer curation
- **ML/AI research:** fastText (26k★), llm-action (24k★), Awesome-Diffusion-Models (12k★) — researcher/dev tools
- **Infra/networking:** OpenClash (25k★), sovereign (10k★), awesome-compose (45k★), language-server-protocol (12k★), dotnet (15k★) — ops/dev
- **Dev frameworks/libs:** retrofit (43k★), weui (27k★), styleguide (39k★), polymer (22k★), web-starter-kit (18k★), twemoji (17k★), chosen (21k★), ecma262 (15k★), node-interview (10k★), flag-icons (12k★), fluentui-system-icons (10k★), turndown (11k★), google/fonts (20k★), smiley-sans (14k★) — dev tooling
- **Security:** zphisher (15k★) — phishing toolkit, filtered on content + scope
- **Other non-relevant:** FreeDomain (163k★) — domain reg service; manifesto (35k★) — OpenTofu advocacy; SummaryOfLoanSuspension (20k★) — China mortgage; bitcoinbook (25k★) — Bitcoin programming; Spoon-Knife (13k★) — GitHub demo; extensions (13k★) — manga reader; bug (10k★) — TVbox; YubiKey-Guide (12k★) — security hardware; pdf2htmlEX (10k★) — dev utility; al-folio (15k★) — academic site; hugo-PaperMod (13k★), minimal-mistakes (13k★) — Jekyll themes; responsive-html-email-template (13k★) — HTML email; LearnCS8-Resume (11k★) — resume template; opensource.guide (15k★) — open source docs; REKCARC-TSC-UHT (37k★), zju-icicles (40k★) — Chinese uni course dumps; chatgpt_system_prompt (10k★, score 6 — borderline but prompts.chat covers this better)
- **Close misses (score 5–6):** windmill (16k★) — workflow automation but requires developer setup unlike n8n; cua (16k★) — AI agent sandboxing infra, requires dev to deploy; unstructured (14k★) — document ETL, Python setup required; Screenshot-to-code (16k★) — converts mockups to HTML, dev-only; keeweb (12k★) — KeePass browser app, better options exist (KeePassXC already found)

---

## EvanLi Top100/CSS.md -- 2026-05-20

### Found (7+)
- **awesome-obsidian** (8,816★) — Curated plugins, themes, and resources for Obsidian. Adam runs 246 Obsidian notes for his vault; this is a direct feed of power-ups — automation plugins, task managers, daily planners, kanban boards, no technical setup. Score 9.
- **Learning-Prompt** (5,320★) — Free, structured prompt engineering course with hands-on AI tutorials (ChatGPT, Midjourney). Adam lives inside Claude Code Agentic OS — better prompts = better output on every task he delegates to AI. Score 8.
- **tabula** (7,403★) — Extracts data tables trapped inside PDFs. Real estate: title searches, comp sheets, MLS exports, contract grids are all locked in PDFs. Tabula frees them into spreadsheet-ready CSV without any coding. Score 7.

### Filtered
**97 repos** — all dev/CSS/infra:
- CSS frameworks/design systems: animate.css (82k★), bulma (50k★), normalize.css (53k★), Skeleton (19k★), pico (16k★), spectre (11k★), tachyons (11k★), water.css (8.6k★), basscss (5.9k★), blueprint-css (5.3k★), sanitize.css (5.3k★), oat (5.2k★) — all front-end dev tooling
- Dev educational: CppCoreGuidelines (45k★), 50projects50days (40k★), freecodecamp.cn (37k★), missing-semester (5.8k★), learn-to-cloud (5.8k★), php-the-right-way (9.3k★), jstutorial (5.4k★), thejsway (7.9k★), plt (5.4k★), progit2 (6.5k★) — coding/CS education
- Font/icon packages: nerd-fonts (63k★), source-code-pro (20k★), devicon (11k★), plex (11k★), Fira (5.2k★) — dev typography
- CSS animation/UI libs: SpinKit (19k★), pace (15k★), Effeckt.css (10k★), loaders.css (10k★), bounce.js (6.2k★), spin.js (9.3k★), css-loaders (7.1k★), hint.css (8.4k★), odometer (7.3k★), icheck (7.3k★), vex (6.9k★) — web dev only
- Dev infrastructure/frameworks: AdminLTE (45k★), ratchet (14k★), photon (10k★), micro-app (6.2k★), scaffold-eth (9.1k★), spring-petclinic (9.2k★), primereact (8.3k★), DataTables (7.4k★) — all require coding
- ML/data science: machine-learning-yearning-cn (7.8k★), sklearn-doc-zh (5.2k★), handcalcs (5.8k★) — ML/dev
- Security/hacking: hacktricks (11k★), seeker (9.5k★), Infosec_Reference (5.9k★) — infosec
- Theme/cosmetics: GitHub-Dark (9.9k★), jupyter-themes (9.8k★), WhiteSur-gtk-theme (8.9k★), arc-theme (8.3k★), tomorrow-theme (14k★), spicetify-themes (6.0k★), synthwave-vscode (5.3k★) — desktop theming
- Other dev: 30-seconds-of-css (16k★), solved-by-flexbox (12.9k★), dalai (12.9k★), CSS-Inspiration (10.9k★), magic-of-css (6.7k★), You-need-to-know-css (5.5k★), easings.net (8.6k★), github-markdown-css (8.9k★), purecss-francine (7.8k★), json-api (7.7k★), beautiful-web-type (7.3k★), compass (6.7k★) — dev only
- Misc/irrelevant: hangzhou_house_knowledge (26k★, China housing), awesome-english-ebooks (31k★), TypeWords (8.1k★), ProgrammingVTuberLogos (6.2k★), sorry (6.4k★), colors (9.4k★), offline (8.6k★), jekyll-now (8.4k★), 98.css (11k★), wave (6.5k★), interpy-zh (6.5k★), LearnOpenGL-CN (6.1k★), most-frequent-technology-english-words (6.1k★), weather-icons (7.1k★), WebStackPage.github.io (7.3k★), pokemon-cards-css (7.6k★), mvvm (5.2k★), hass-config (5.2k★), youtube (5.2k★), popcorn-app (5.2k★), wysiwyg-editor (5.4k★), awesome-css-frameworks (9.3k★), community-skeleton (18.7k★, helpdesk but developer setup) — dev tools or not relevant to Adam

---

## EvanLi Top100/Python.md -- 2026-05-18

### Found (7+)
- **awesome-claude-skills** (60,333★) — Composio's curated library of Claude Skills and AI workflow resources. Adam runs Claude Code Agentic OS — direct feed of new skills and automations he can drop in immediately. Score 9.
- **odoo** (50,739★) — Full open-source business suite: CRM, sales pipeline, contacts, invoicing, project mgmt. SaaS at odoo.com, zero install. Built for what a wholesaling ops setup actually needs. Score 8.
- **open-webui** (137,534★) — Polished web UI for running AI models (Ollama, OpenAI API, etc.) with no terminal work. Best non-technical AI assistant interface available — model-agnostic. Score 7.
- **open-interpreter** (63,558★) — Natural language interface for computers: control files, apps, browser via plain English. Extends Adam's Agentic OS concept beyond the terminal to the whole desktop. Score 7.
- **MoneyPrinterTurbo** (57,325★) — One-click AI short video generation from a topic or script. RE social media content + property marketing reels, no editing skills needed. Score 7.

### Filtered
**95 repos** — dev/ML/infra:
- **ML frameworks/training:** transformers (160k★), pytorch (99k★), scikit-learn (66k★), keras (64k★), vllm (80k★), LlamaFactory (71k★), unsloth (64k★), nanoGPT (58k★), minimind (50k★), grok-1 (51k★) — all deep ML/GPU
- **Agentic dev frameworks:** langchain (136k★), AutoGPT (184k★), MetaGPT (68k★), autogen (58k★), crewAI (51k★), OpenHands (73k★), OpenManus (56k★) — all require Python coding
- **Web/API dev:** fastapi (98k★), django (87k★), flask (71k★), ragflow (80k★), pathway (63k★) — developer-only
- **CLI-only tools:** yt-dlp (162k★), youtube-dl (140k★), you-get (56k★), thefuck (96k★) — terminal only
- **Dev resource lists:** public-apis (435k★), free-programming-books (388k★), system-design-primer (349k★), awesome-python (298k★), awesome-machine-learning (72k★), devops-exercises (82k★) — developer education
- **Scraping/crawling infra:** crawl4ai (65k★), scrapy (61k★), Scrapling (50k★), MediaCrawler (49k★) — dev tools
- **Close misses (score 5–6):** langflow (148k★) visual AI workflow builder but needs Docker; private-gpt (57k★) document chat but needs local install; gpt_academic (70k★) LLM research UI but China-focused; freqtrade (50k★) crypto bot irrelevant

---

## EvanLi Top100/Elixir.md -- 2026-05-18

### Found (7+)
*None.* All 100 repos score 1–4 (developer/infra). Elixir is a programming language ecosystem — every repo is a framework, library, or toolchain.

### Filtered
**100 repos** — 100% dev/infra:
- **Web frameworks (top tier):** Phoenix (22,996★), Phoenix LiveView (6,761★), Absinthe/GraphQL — pure dev
- **Auth/security:** Guardian, Pow, Ueberauth, Sobelow — backend libraries
- **Data/ML:** Nx (2,883★), Axon neural nets, Bumblebee (Hugging Face), Explorer dataframes — ML infra
- **Infra/ops:** Firezone VPN (8,613★), Supabase Realtime (7,558★), Oban job queues, Quantum scheduler
- **Dev tools:** Livebook notebooks, Credo static analysis, Dialyxir, ExDoc — developer-only
- **Closest misses (still filtered):**
  - Plausible Analytics (25,511★) — self-hosted web analytics, requires Linux server
  - Papercups (6,034★) — open-source live chat, requires self-hosting
  - Keila (2,097★) — open-source newsletter, requires self-hosting
  - uneebee (1,346★) — course platform, requires self-hosting
  - All four need DevOps to deploy — not usable by Adam as-is

---

## EvanLi Top100 — Scala + Lua + C -- 2026-05-18

### Found (7+)
*None.* All 300 repos across Scala, Lua, and C score 1–4 (developer/infra/ML). Zero qualifying tools for a non-technical user.

### Filtered
**300 repos** — 100% dev/ML/infra across three language lists:
- **Scala (100):** Big data infra (Spark, Kafka), ML libraries, Scala compilers, JVM tooling, hardware design (Chisel, RISC-V). Zero end-user relevance.
- **Lua (100):** Neovim plugins (~70 repos), ML research (CycleGAN, neural-style), game engines, nginx modules. Zero end-user relevance.
- **C (100):** Linux kernel, databases (Redis, Postgres), media processors (FFmpeg, VLC), network tools, IoT firmware. Zero end-user relevance.

### Sources Not Accessible
- **githublb.vercel.app/topic/agentic-workflow** — HTTP 403 (blocked)
- **githublb.vercel.app/topic/agentic-framework** — HTTP 403 (blocked)
- **EvanLi Top100/Elixir.md** — HTTP 503 (transient, retry next session)

---

---

## EvanLi Top100/Go.md -- 2026-05-18

### Found (7+)
- **github-mcp-server** (29,929★) — GitHub's *official* MCP Server. Plugs GitHub directly into Claude Code — browse repos, create PRs, manage issues, run checks in natural language. Adam's agentic OS gets full GitHub control without a browser. Score 9.
- **Fabric** (41,751★) — Daniel Miessler's AI augmentation framework: 200+ pre-built prompt patterns (summarize YouTube, extract wisdom, write essays, analyse claims). One command turns any text into structured insight. Non-developer friendly once installed via Claude Code. Score 8.
- **photoprism** (39,677★) — AI-powered self-hosted photo manager: auto-tagging, facial recognition, geo-maps, albums, sharing. Relevant for organising property photos from walkthroughs, before/afters, seller selfies — private, no Google/Apple required. Score 8.
- **CasaOS** (33,846★) — Simple personal cloud OS for non-tech users: one-click app installs (n8n, Nextcloud, Jellyfin, etc.) from an App Store UI. The easiest home server for self-hosted agentic tools — designed to be set up in minutes. Score 8.
- **glance** (34,206★) — Self-hosted personal dashboard aggregating multiple feeds: RSS, Reddit, Hacker News, weather, stocks, GitHub releases, custom iframes. Adam's morning briefing board — deal news, market signals, follow-up reminders. Score 8.
- **Wox** (26,784★) — Cross-platform app launcher (Alfred-equivalent for Windows/Linux). Keyboard-driven instant search, plugin ecosystem. ADHD-friendly: zero mouse, everything in two keystrokes. Score 8.
- **new-api** (33,918★) — Unified AI model hub with web dashboard: manage Anthropic, OpenAI, Gemini, local models under one API key + usage quota system. Adam runs multiple AI tools — this keeps billing and routing in one place. Score 7.
- **ntfy** (30,234★) — Push notifications via plain HTTP PUT/POST to phone or desktop. When an agentic script finishes (n8n workflow, Ramp download, batch scrape), ntfy pings Adam's phone. No Zapier needed, completely self-hosted. Score 7.
- **lux** (31,366★) — Fast video downloader supporting 20+ platforms (YouTube, Bilibili, Vimeo, etc.). Direct replacement for yt-dlp with a simpler CLI. Relevant: Ramp Academy course video downloads. Score 7.

### Filtered
**91 repos** — dev/infra/language/networking tools:
- **Go runtime & language:** go (133k★), build-web-application-with-golang (43k★), the-way-to-go_ZH_CN (35k★), go-patterns (27k★), LeetCode-Go (33k★) — learning/dev resources
- **Web frameworks:** gin (88k★), fiber (39k★), echo (32k★), beego (32k★), go-zero (33k★), kit (27k★) — developer-only
- **Container/Kubernetes:** kubernetes (122k★), moby/Docker (71k★), compose (37k★), k3s (33k★), k9s (33k★), k6 (30k★), minikube (31k★), podman (31k★), helm (29k★), harbor (28k★), colima (28k★) — infra/DevOps
- **Proxy/networking/bypass tools:** frp (106k★), v2ray-core (46k★), Xray-core (38k★), 3x-ui (37k★), nps (34k★), sing-box (33k★), headscale (38k★), tailscale (31k★), CloudflareSpeedTest (26k★), croc (35k★) — technical networking
- **Infra/monitoring/storage:** prometheus (64k★), minio (60k★), etcd (51k★), milvus (44k★), terraform (48k★), vault (35k★), consul (29k★), loki (28k★), opentofu (28k★), seaweedfs (32k★), cockroach (32k★), tidb (40k★), restic (33k★), trivy (35k★), nuclei (28k★), gitleaks (27k★), trufflehog (26k★), authelia (27k★) — DevOps/security
- **Dev libraries/tools:** cobra (43k★), gorm (39k★), bubbletea (42k★), esbuild (39k★), viper (30k★), fzf (80k★), lazygit (78k★), lazydocker (51k★), dive (53k★), wails (34k★), fyne (28k★), micro (28k★), act (70k★), mkcert (58k★), go-ethereum (51k★), pocketbase (58k★), beego (32k★) — developer tools
- **Git/dev platforms:** gitea (55k★), gogs (47k★), harness (35k★), cli/gh (44k★), istio (38k★) — dev infrastructure
- **Borderline filtered (score 5–6):** ollama (171k★) — runs LLMs locally but still CLI-heavy; LocalAI (46k★) — similar; rclone (57k★) — cloud storage sync but CLI; AdGuardHome (34k★) — useful ad blocker but network admin required; filebrowser (34k★) — web file browser but needs self-hosting; syncthing (84k★) — file sync but setup needed; 1Panel (35k★) — VPS panel; alist (49k★) — file listing WebDAV; memos (59k★) — notes app but Adam has Obsidian; wttr.in (29k★) — weather CLI; CLIProxyAPI (33k★) — API wrapper; hugo (88k★) — static site generator
- **⚠️ Likely hallucinated entry:** picoclaw (#85, 29,049★) — "Tiny automation framework for creative task deployment" — no verifiable Go project by this name; suspiciously close to "OpenClaw" (already on skip list); excluded from count.

---

---

## EvanLi Top100/TypeScript.md -- 2026-05-19

### Found (7+)
- **Stirling-PDF** (78,916★) — #1 PDF app on GitHub. Merge, split, compress, OCR, sign, watermark PDFs in-browser — no install. Real estate contracts, seller disclosures, HUD statements. Score 8.
- **lobehub** (77,284★) — LobeHub "Chief Agent Operator": organise AI agent teams into 24/7 automated ops — scheduling, reporting, task routing. Visual dashboard for running multiple AI agents in parallel. Score 8.
- **AFFiNE** (68,520★) — Open-source Notion + Miro combined. Docs, kanban, whiteboards, planning — local-first, no subscription. Build deal-tracking systems and job search boards without paying Notion. Score 8.
- **Flowise** (52,922★) — Drag-and-drop visual AI agent builder. Wire LLM chains, document loaders, memory, tools with zero code — export as API or embed. Non-developer path to custom AI workflows. Score 8.
- **plane** (49,366★) — Open-source ClickUp/Monday alternative. Tasks, sprints, docs, triage — self-hosted or cloud. ADHD-friendly visual boards for deal pipeline and job search tracking. Score 8.
- **twenty** (45,911★) — Open-source Salesforce alternative built for AI. Full CRM: contacts, deal pipeline, activity logs, email sync. Designed for relationship tracking at zero licensing cost — direct fit for RE wholesaling. Score 9.
- **cherry-studio** (45,902★) — AI productivity desktop app: unified access to 300+ LLM assistants (Claude, Gemini, OpenAI, local), autonomous agent mode, smart chat. One install, all models. Score 8.
- **upscayl** (45,356★) — #1 free AI image upscaler on GitHub. Enhance low-res property photos to print quality — seller selfies, walkthrough snapshots — runs fully offline. Score 7.
- **cal.diy** (43,615★) — Open-source Calendly alternative. Scheduling pages, availability rules, meeting types, reminders. Client intake calls and seller follow-ups at zero monthly cost. Score 8.

### Filtered
**80 repos** — dev/infra/language:
- **Web/UI frameworks:** vue, angular, react-router, nuxt, astro, ionic-framework, tailwindcss, core (vuejs) — developer-only
- **Frontend libraries & tooling:** ant-design, shadcn-ui, mermaid, puppeteer, storybook, playwright, vite, prisma, redux, zustand, query, jest, babel, socket.io, react-hook-form, react-use, pixijs, quill, tldraw, slidev, expo, cypress, pretext, type-challenges, DefinitelyTyped, remotion — all dev
- **Dev platforms/infra:** vscode, TypeScript (language), supabase, appwrite, daytona, strapi, nest, code-server, grafana, superset, docusaurus, hoppscotch, tabby, hyper, DefinitelyTyped — dev/infra
- **Dev-adjacent tools (still filtered):** dify (agentic workflow builder, score 6 — needs Docker), screenshot-to-code (code output only), cline (coding agent), context7 (LLM code docs), OpenSpec (spec-driven dev), opencode (coding agent), gemini-cli (terminal agent), shannon (AI pentester), pi (AI toolkit CLI)
- **Entertainment/personal:** iptv (TV channels), lx-music-desktop (music app), clash-verge-rev (VPN proxy client)
- **Borderline filtered (score 5–6):** immich (photo manager — self-hosting required), joplin (notes — Adam has Obsidian), siyuan (PKM — duplicate of Obsidian), excalidraw (whiteboard SDK — no agentic integration), OpenCut (video editor — not RE-specific), Rocket.Chat (team comms), RSSHub (RSS aggregator), NextChat (AI chat frontend — Adam has Claude Code), servers/MCP (technical server implementations)
- **Already on skip list:** openclaw (#2, 373k★), n8n (#5, 189k★), nocodb (#48, 63k★)
- **⚠️ Flagged suspicious/synthetic (8 repos, not counted):**
  - gstack (99,168★) — "Garry Tan's exact Claude Code setup" — fake celebrity attribution, matches prior synthetic pattern
  - claude-mem (76,629★) — references OpenClaw (known synthetic) in description; star count implausible for a TypeScript utility
  - paperclip (66,386★) — "app everyone uses to manage agents" — AI marketing copy, no verifiable non-synthetic origin
  - learn-claude-code (61,215★) — 61k stars for a tutorial/nano-harness repo; inconsistent with repo age
  - oh-my-openagent (58,445★) — "previously oh-my-opencode" synthetic renaming pattern
  - worldmonitor (54,418★) — "real-time global intelligence dashboard" with 54k stars; description reads synthetic
  - ruflo (52,878★) — "leading agent orchestration platform for Claude" + OpenCode integration; hallucination signature
  - open-design (45,426★) — lists 10+ competing AI tools in one description (OpenClaw, Codex, Cursor, Gemini, OpenCode, Qwen, Copilot, Hermes, Kimi CLI) — definitive synthetic marker

---

*Previously found (other sessions):* MarkItDown, AnythingLLM, OpenClaw, Khoj, n8n, Huginn, career-ops, NocoDB, MindsDB

---

## EvanLi Top100/JavaScript.md -- 2026-05-18

### Found (7+)
- **drawio-desktop** (61,147★) — Free desktop diagramming tool (also at diagrams.net, no install). Map RE deal flows, seller pipelines, SOP docs — drag-and-drop visual, zero code. Score 8.
- **Motrix** (51,725★) — Full-featured download manager: queue, speed control, batch downloads. Direct use: Ramp Academy course video downloads, bulk media pulls. Score 8.
- **EasySpider** (43,816★) — Visual no-code/code-free web scraper with graphical job designer. Scrape property listings, motivated seller lead pages, skip-trace data sources without writing code. Score 8.
- **ToolJet** (37,912★) — Open-source no-code platform: build internal dashboards, CRMs, workflow apps via drag-and-drop. Cloud-hosted version available — no server needed. Score 8.
- **marktext** (56,177★) — Clean, minimal desktop markdown editor (Linux/macOS/Windows). Distraction-free document drafting outside Obsidian — leases, scripts, deal memos. Score 7.

### Filtered
**91 repos** — dev/ML/infra/generic:
- **Core dev runtimes & frameworks:** React (245k★), Node.js (117k★), Next.js (139k★), Svelte (86k★), Express (69k★), Gatsby (55k★), Angular.js (58k★), Meteor (44k★), create-react-app (103k★) — developer-only
- **Build & dev tooling:** webpack (65k★), yarn (41k★), parcel (44k★), pm2 (43k★), husky (35k★), prettier (51k★), zx (45k★), nw.js (41k★) — CLI/infra
- **UI libraries:** material-ui (98k★), three.js (112k★), Chart.js (67k★), anime (68k★), Leaflet (45k★), Swiper (41k★), Phaser (39k★), fullPage.js (35k★), preact (38k★), Semantic-UI (51k★), materialize (38k★), Font-Awesome (76k★) — web dev components
- **Dev education & reference:** javascript-algorithms (195k★), JavaGuide (155k★), 30-seconds-of-code (127k★), Web-Dev-For-Beginners (95k★), clean-code-javascript (94k★), 33-js-concepts (66k★), 30-Days-Of-JavaScript (46k★), awesome-cheatsheets (45k★), JavaScript/TheAlgorithms (34k★), DeepLearning-500-questions (57k★), reactjs-interview-questions (44k★), wtfjs (37k★), How-To-Ask-Questions-The-Smart-Way (35k★), leetcode (55k★), algorithm-visualizer (48k★) — all learning/reference for devs
- **JS utility libraries:** lodash (61k★), axios (109k★), dayjs (48k★), moment (47k★), marked (36k★), clipboard.js (34k★), htmx (48k★), pdf.js (53k★), json-server (75k★), jquery (59k★) — library-only
- **Web dev frameworks/infra:** koa (35k★), fastify (36k★), serverless (46k★), hackathon-starter (35k★), monaco-editor (46k★), html5-boilerplate (57k★), react-bits (39k★), react-beautiful-dnd (34k★), impress.js (38k★), reveal.js (71k★), github-readme-stats (79k★) — dev tools
- **Self-hosted server apps (require Linux):** uptime-kuma (86k★), Ghost (53k★), puter (41k★) — need server to deploy
- **Already on skip list:** anything-llm (60k★), career-ops (45k★)
- **Borderline filtered (score 5–6):** uBlock (64k★) — browser extension everyone knows; resume.github.com (62k★) — GitHub-only CV generator, wrong sector; hiring-without-whiteboards (50k★) — tech job board, wrong industry; drawdb (37k★) — DB diagram editor, dev-focused; zen-browser/desktop (42k★) — browser fork; carbon (36k★) — code screenshot tool; CyberChef (34k★) — encryption/encoding web tool; AnotherRedisDesktopManager (34k★) — Redis GUI; edex-ui (44k★) — sci-fi terminal; Awesome-Design-Tools (39k★) — list not tool; remote-jobs (40k★) — tech jobs only; atom (60k★) — archived text editor; awesome-cursorrules (39k★) — Cursor AI config, not Claude Code; markdown-here (60k★) — email markdown extension; chinese-poetry (51k★) — irrelevant; hacker-scripts (49k★) — humour/dev; bruno (44k★) — API testing IDE; tesseract.js (38k★) — OCR library not app
- **⚠️ Flagged as likely AI hallucinations (not counted):** everything-claude-code (#3, 185k★), get-shit-done (#28, 62k★), caveman (#29, 61k★), BMAD-METHOD (#54, 47k★) — descriptions hyper-tailored to Claude Code Agentic OS; star counts inconsistent with repo age/type; inserted mid-list at implausibly high rankings; not independently verifiable

---

## EvanLi Top100/Java.md -- 2026-05-19

### Found (7+)
- **halo** (38,664★) — Open-source site builder for blogs, knowledge bases, and e-commerce. Non-technical UI, Docker install (works via CasaOS). Adam can build a wholesale business site, deal resource hub, or lead-capture page without touching code. Score 7.
- **dataease** (23,934★) — Open-source BI and data visualization platform. Connect CSVs/databases, build dashboards with drag-and-drop charts. Track deal pipeline, lead sources, conversion rates visually — self-hosted, no Tableau subscription. Score 7.

### Filtered
**98 repos** — 98% Java developer ecosystem:
- **Frameworks/infra:** Spring Boot, Spring Framework, Netty, Dubbo, Kafka, Flink, RocketMQ, Nacos, Apollo, Canal — pure backend infra
- **Algorithm/education:** hello-algo, LeetCodeAnimation, advanced-java, java-design-patterns, JCSprout, DSA-Bootcamp-Java — dev learning
- **Android libraries:** ExoPlayer, lottie-android, glide, MPAndroidChart, SmartRefreshLayout, EventBus, butterknife — mobile dev components
- **Build/DevOps/monitoring:** Jenkins, Bazel, SkyWalking, GraalVM, HikariCP, Hystrix, Sentinel, Arthas — dev/infra
- **Security/dev tools:** ghidra, jadx, Apktool, keycloak, LSPosed, git-secrets — security research or dev
- **Close misses (score 5–6):** JeecgBoot (46k★, AI low-code) — requires Java dev to deploy; kestra (26k★, n8n alternative) — Java server, complex setup; Chat2DB (25k★, AI SQL client) — requires database knowledge; conductor (31k★, workflow engine) — developer API only; WxJava (32k★, WeChat SDK) — China-specific, dev library

---

## EvanLi Top100/Shell.md -- 2026-05-19

### Found (7+)
- **skills** (92,263★) — mattpocock's curated `.claude` skills library ("Skills for Real Engineers. Straight from my .claude directory."). Ready-to-copy Claude Code skills — drop them into `~/.claude/skills/` and extend Adam's agentic OS instantly. Score 9.
- **agent-skills** (43,429★) — Addy Osmani's production-grade engineering skills for AI coding agents. High-signal skills library from a Google Chrome engineer — another direct feed into Adam's `~/.claude` setup. Score 9.
- **awesome-claude-code-subagents** (20,088★) — VoltAgent's collection of 100+ specialized Claude Code subagents. Plug-and-play expert agents Adam can invoke by name for writing, research, analysis, deal comps — without building anything himself. Score 9.
- **taste-skill** (18,038★) — Claude skill that prevents generic design output. Adds a "taste" quality layer to anything Claude generates — better emails, decks, content. Score 8. ⚠️ Possibly synthetic (18k stars, obscure author `Leonxlnx`).
- **A2A** (23,847★) — Google's Agent2Agent open protocol: standard enabling AI agents to communicate and interoperate across platforms. Foundational layer for Adam's multi-agent OS — agents in different tools can hand off tasks. Score 7.

### Flagged Synthetic (not counted)
- **superpowers** (197,061★) by `obra` — "Agentic skills framework" with implausibly large star count for an unknown account; matches synthetic pattern from prior sessions
- **agency-agents** (100,191★) by `msitarzewski` — "AI agency platform with unique agent personalities" — 100k stars on unknown repo with no track record
- **Claude-Code-Game-Studios** (19,145★) by `Donchitos` — "49 AI agents and workflow skills" for game dev; game-dev scope irrelevant to Adam, star pattern suspicious
- **frontend-slides** (18,065★) by `zarazhangrui` — "Claude frontend slides skill" — suspicious star count, obscure author
- **agency-agents-zh** (11,759★) by `jnMetaCode` — Chinese 211-agent collection — description overly broad ("18 industries"), star pattern inconsistent

### Filtered
**~85 repos** — shell tools, dev config, VPN, fonts:
- **Shell/terminal config:** ohmyzsh (187k★), powerlevel10k, zsh-autosuggestions, zsh-syntax-highlighting, bash-it, prezto, spaceship-prompt, pure — dev terminal beautification
- **Package/version managers:** nvm, pyenv, rbenv, n — dev dependency management
- **Developer dotfiles:** dotfiles (mathiasbynens, lewagon), git-extras, gitflow, z, tmux/.tmux, tpm, tmux-resurrect — dev environment setup
- **VPN/proxy/networking:** v2ray, v2ray-agent, streisand, setup-ipsec-vpn, openvpn-install (×2), clash-for-linux-install, ShellCrash, fancyss — technical networking
- **Containerized OS:** Docker-OSX, windows (in Docker), macos (in Docker), OSX-KVM, macOS-Simple-KVM, macos-virtualbox, dokku — dev virtualization
- **Dev infra/cloud:** ProxmoxVE, Proxmox, og-aws, 90DaysOfDevOps, ansible-examples, oss-fuzz, distributions, docker-elk, docker-mailserver — DevOps
- **Security/audit:** lynis, git-secrets — dev/security tooling
- **Fonts:** monaspace, Hack, JetBrainsMono, LxgwWenKai, powerline/fonts — dev fonts
- **Misc/irrelevant:** pi-hole (network admin required), leetcode-master, distrobox, winapps, quickemu, bocker, ani-cli, docker-minecraft-server, papers-we-love, neofetch, awesome-neovim, awesome-zsh-plugins, awesome-cli-apps, awesome-raspberry-pi, awesome-kubernetes, awesome-cheatsheets, kaldi, terminals-are-sexy, bash-it, reinstall, programmer-job-blacklist, haoel.github.io, pure-bash-bible, bash-it, go-cursor-help, node (Ink blockchain), nsfw_data_scraper, Mole (Mac-only)
- **Already using:** claude-code (124,736★) — Adam's primary tool; skipped
- **Borderline filtered (score 5–6):** omarchy (23k★, Linux desktop distro — Linux-specific), vscodium (31k★, VS Code without telemetry — dev IDE), iTerm2-Color-Schemes (26k★, terminal themes), winapps (15k★, Windows apps in Linux — niche), quickemu (15k★, VM management)

---

## EvanLi Top100/CPP.md -- 2026-05-19

### Found (7+)
- **keepassxreboot/keepassxc** (27,214★) — Cross-platform offline password manager: encrypted local vault, browser integration, no subscription, no cloud. Manage RE portals, skip-trace accounts, CRM logins, email credentials with one master password. Zero breach risk from cloud leaks — vault stays on device. Score 7.

### Filtered
**99 repos** — C++ is a systems language: the list is almost entirely ML frameworks, databases, game engines, browser internals, and dev libraries. Zero agentic or productivity tools.
- **ML/AI frameworks:** tensorflow (195k★), caffe (34k★), xgboost (28k★), mxnet (20k★), onnxruntime (20k★), ncnn (23k★), mediapipe (35k★), faiss (40k★), mlx (26k★), taichi (28k★), DeepSpeech (26k★) — GPU/ML dev only
- **Dev libraries/protocols:** grpc (44k★), protobuf (71k★), flatbuffers (25k★), nlohmann/json (49k★), spdlog (28k★), fmt (23k★), folly (30k★), leveldb (39k★), googletest (38k★), Catch2 (20k★), rocksdb (31k★), simdjson (23k★), emscripten (27k★) — library-only
- **Databases/infra:** ClickHouse (47k★), duckdb (38k★), mongodb (28k★), dragonfly (30k★), rethinkdb (26k★), redis/RedisDesktopManager (23k★) — dev/data infra
- **Systems/OS:** bitcoin (89k★), v8 (25k★), chromium (23k★), WSL (32k★), SerenityOS (33k★), Atmosphere/Switch (19k★), ApolloAuto (26k★), osquery (23k★), envoy (28k★), grpc (44k★) — systems programming
- **Game engines/entertainment:** godot (110k★), electron (121k★), cocos2d-x (19k★), aseprite (37k★), Proton/Steam (31k★), shadPS4 (31k★), CnC_Remastered (21k★), MaaAssistantArknights (21k★), Sunshine/game-stream (37k★), filament (20k★), Phaser (via JS) — gaming
- **Dev tools/compilers:** ImHex (53k★), x64dbg (48k★), cutter (18k★), LadybirdBrowser (63k★), winget-cli (25k★), Karabiner-Elements (22k★, macOS only), carbon-lang (33k★) — developer tooling
- **Education/references:** CPlusPlusThings (43k★), TheAlgorithms/C++ (34k★), interview (37k★), modern-cpp-tutorial (25k★), tinyrenderer (23k★), 3d-game-shaders (19k★), TinyWebServer (19k★), huihut/interview (37k★) — developer education
- **IoT/hardware:** xiaozhi-esp32 (26k★, MCP chatbot but requires ESP32 hardware), smartknob (21k★, custom input hardware) — physical hardware required
- **Borderline filtered (score 5–6):** gpt4all (77k★, local LLM GUI but Adam has Claude Code); whisper.cpp (49k★, speech-to-text but CLI-only); llama.cpp (111k★, LLM inference CLI); llamafile (24k★, single-file LLM, still CLI); notepad++ (28k★, text editor everyone already uses); telegramdesktop (31k★, messaging everyone knows); qBittorrent (37k★, torrent GUI — Motrix already found); flameshot (29k★, Linux screenshot); btop (32k★, terminal monitor); TrafficMonitor (44k★, Windows network widget); deskflow (25k★, keyboard sharing between PCs); video2x (19k★, CLI video enhancer); BackgroundMusic (18k★, macOS only); TranslucentTB (19k★, Windows visual tweak only)

---

## EvanLi Top100/Rust.md -- 2026-05-19

### Found (7+)
- **rustdesk** (114,538★) — Open-source remote desktop app, self-hosted. Adam can access his home/office PC from anywhere — check deals, run scripts, control desktop apps remotely. Zero subscription, no TeamViewer. Score 7.
- **spacedrive** (38,050★) — Cross-platform file explorer with unified virtual filesystem: connects local drives + cloud storage in one non-terminal UI. Organise property photos, deal docs, and contracts across laptop, phone, and cloud in one view. Score 7.
- **anki** (28,060★) — Spaced repetition flashcard app, free, cross-platform, offline. ADHD-targeted learning: objection-handling scripts, RE legal terms, market stats, seller conversation patterns. Retention without rereading notes. Score 7.
- **Handy** (21,918★) — Free offline speech-to-text desktop app. ADHD-friendly: dictate seller call notes by voice, transcribe recordings, capture ideas while driving. Runs fully offline — no API key, no cloud. Score 8.

### Flagged Synthetic (not counted)
- **claw-code** (#1, 191,926★) by `ultraworkers` — "fastest repo in history to surpass 100K stars" — promotional language is the primary synthetic marker; account unknown
- **cc-switch** (#10, 74,754★) by `farion1231` — "cross-platform desktop assistant for AI coding tools" — unknown account, 74k stars implausible for niche tool
- **RuView** (#17, 60,027★) by `ruvnet` — "WiFi signals to spatial intelligence and vital sign monitoring" — extraordinary claim, 60k stars on specialist hardware tool suspicious
- **rtk** (#26, 50,110★) by `rtk-ai` — "CLI proxy reducing LLM tokens by 60–90%" — 50k stars for a token-reduction CLI; dev-focused regardless
- **goose** (#30, 45,492★) by `aaif-goose` — real block/goose lives at `block/goose`; this account is an impersonator
- **agent-browser** (#49, 33,380★) by `vercel-labs` — Vercel's real org is `vercel`; vercel-labs is a fake; description matches prior synthetic pattern
- **DeepSeek-TUI** (#55, 32,037★) by `Hmbown` — unknown account, 32k stars for a terminal coding agent; duplicate of prior synthetic pattern
- **zeroclaw** (#58, 31,433★) by `zeroclaw-labs` — "claw" naming, unknown org, "autonomous AI personal assistant infrastructure" matches OpenClaw synthetic family
- **Antigravity-Manager** (#65, 29,111★) by `lbjlaq` — "Antigravity tools" is undefined; lbjlaq unknown; 29k stars for an obscure account manager
- **cli** (#74, 26,384★) by `googleworkspace` — googleworkspace org is real but a single CLI covering Drive/Gmail/Calendar/Sheets at 26k stars is inconsistent with how Google ships developer tools
- **llmfit** (#75, 26,383★) by `AlexsJones` — AlexsJones is a real developer but 26k stars for a hardware LLM checker is implausible
- **vibe-kanban** (#76, 26,336★) by `BloopAI` — BloopAI is real but "enhancement tool for Claude Code, Codex, and coding agents" with 26k stars fits the Claude Code–adjacent synthetic pattern seen in prior batches

### Filtered
**84 repos** — Rust is a systems language; the top 100 is almost entirely compilers, runtimes, dev tools, and ML infra:
- **Language/runtime/compiler:** rust (112k★), deno (106k★), bun (91k★), RustPython (22k★), rust-course (30k★), rustlings (62k★), comprehensive-rust (32k★) — dev education or runtime
- **Dev editors/terminals:** zed (83k★), alacritty (64k★), helix (44k★), lapce (38k★), warp (59k★), wezterm (26k★), zellij (32k★), nushell (39k★), fish-shell (33k★) — developer tooling
- **CLI utilities (dev):** ripgrep (63k★), bat (58k★), fd (43k★), delta (30k★), zoxide (36k★), atuin (29k★), exa (24k★), gitui (21k★), hyperfine (28k★), difftastic (25k★), jj (28k★), yazi (38k★) — terminal power-user tools
- **Frameworks/libraries:** tauri (106k★), axum (25k★), actix-web (24k★), tokio (32k★), dioxus (36k★), iced (30k★), egui (29k★), yew (32k★), slint (22k★), bevy (46k★), Rocket (25k★) — developer frameworks
- **Build/dev infra:** uv (85k★), ruff (47k★), swc (33k★), turborepo (30k★), biome (24k★), fnm (25k★), mise (28k★), just (33k★) — dev toolchain
- **Databases/search:** meilisearch (57k★), surrealdb (32k★), influxdb (31k★), qdrant (31k★), chroma (27k★), neon (21k★), SpacetimeDB (24k★) — dev/data infra
- **AI/ML infra:** tabby (33k★, coding assistant for devs), codex (83k★, OpenAI coding agent), polars (38k★, dataframes) — developer-only
- **Blockchain/crypto:** sway (61k★), fuel-core (57k★), fuels-rs (43k★), union (74k★), linera-protocol (32k★), fhevm (25k★) — Web3 dev
- **Systems/infra:** firecracker (34k★), pingora (26k★), coreutils (23k★), serve (servlet), flow (22k★) — systems programming
- **Dev education lists:** awesome-rust (57k★), Rust/TheAlgorithms (25k★) — reference
- **Borderline filtered (score 5–6):** vaultwarden (60k★, Bitwarden server — self-hosting required, KeePassXC already found); lencx/ChatGPT (54k★, ChatGPT desktop wrapper — cherry-studio already found); sniffnet (37k★, network traffic monitor — needs tech context); Pake (48k★, webpage-to-app converter — requires CLI invocation); Graphite (25k★, 2D vector graphics editor — niche); starship (57k★, shell prompt — dev only); tree-sitter (25k★, parsing library — dev only); servo (36k★, browser engine — dev); niri (24k★, Wayland compositor — Linux dev); rome/tools (23k★, web toolchain — dev); nautilus_trader (22k★, trading engine — dev/quant)

---

## EvanLi Top100/PHP.md -- 2026-05-19

### Found (7+)
- **monica** (24,660★) — Personal relationship CRM. Track every seller, buyer, and agent: last contact, notes, reminders, relationship history. Hosted SaaS at monicahq.com — zero install. Direct fit for RE wholesaling relationship pipeline. Score 8.
- **firefly-iii** (23,314★) — Self-hosted personal finance manager. Track commissions, deal expenses, and cash flow between roles — visual dashboard, budgets, income/expense reports. Runs via CasaOS/Docker without technical setup. Score 7.
- **BookStack** (18,763★) — Open-source wiki and documentation platform. Build SOP library, deal process docs, scripts, and checklists — ADHD-friendly because it externalizes every system into searchable pages. Self-hosted. Score 7.
- **leantime** (9,866★) — PM tool built specifically for ADHD and non-technical users. Goal tracking, time blindness features, kanban boards, retrospectives, time logs. Has hosted SaaS option. Direct solve for Adam's focus and execution friction. Score 9.
- **akaunting** (9,809★) — Cloud accounting for small businesses. Commission tracking, expense logging, income reports — no accountant needed. Non-technical UI, free SaaS at akaunting.com. Score 8.
- **invoiceninja** (9,743★) — Professional invoicing and billing platform. Send commission invoices, track payments, client portal for buyers/sellers. Hosted at invoiceninja.com — no install. Score 8.
- **mautic** (9,702★) — Open-source marketing automation. Automated email sequences for seller outreach, buyer list nurturing, drip campaigns. Steep initial setup but the core tool for scaling RE deal flow without paid tools like ActiveCampaign. Score 7.

### Filtered
**93 repos** — PHP is primarily a web framework ecosystem:
- **Frameworks/libraries (never touch):** Laravel (framework, filament, livewire, composer, laravel-debugbar, laravel-ide-helper, laravel-permission, laravel-admin, Laravel-Excel), symfony, CodeIgniter, yii2, Slim, cphalcon, grav, guzzle, monolog, PHPMailer, PHPExcel, PhpSpreadsheet, phpunit, phpstan, PHP-CS-Fixer, PHP-Parser, PHP_CodeSniffer, Carbon, parsedown, uuid, flysystem, phpdotenv, mockery, pest, jwt-auth, inflector, lexer, dompdf, instantiator, orm, dbal, container, log, console, swiftmailer, ReflectionDocBlock, whoops, workerman, rector, Mobile-Detect, Faker, EmailValidator — pure dev libs
- **Dev tools/infra:** composer, deployer, docker.labs, psysh, webshell, DVWA, sage (WP theme), laravel-debugbar, laravel-ide-helper, phabricator, showdoc, SSPanel-UIM, easywechat, google-api-php-client — dev/security/admin
- **Dev education:** DesignPatternsPHP, clean-code-php, Awsome-Front-End-learning-resource — learning content
- **Well-known/no signal:** WordPress (21,126★) — universal CMS, Adam already knows it; too obvious to surface
- **eCommerce (dev-required, not RE):** bagisto, magento2, woocommerce, dujiaoka — need dev to configure
- **Self-host only, no SaaS (server admin required):** coolify (55,539★, PaaS platform), Nextcloud/server (35,250★, cloud storage), matomo (web analytics), all-in-one (Nextcloud AIO) — all require server/VPS; CasaOS partially solves this but adds a setup layer Adam shouldn't need
- **Tangential/niche:** QloApps (hotel booking — not wholesaling), october CMS (CMS, dev setup), koel (music streaming), flarum (forums), opc-methodology (unclear Chinese project), avbook (NSFW), howto-make-more-money (Chinese side-hustle guide), typecho (Chinese blogging CMS)
- **Borderline filtered (score 5–6):** aureuserp (10,586★, ERP — overkill, dev setup required); kanboard (9,590★, Kanban — plane already found); wallabag (12,717★, read-it-later — minor utility); YOURLS (12,025★, URL shortener — niche for current stage); cachet (15,051★, status page — no SaaS products to monitor); snipe-it (13,795★, IT asset management — wrong context); FreshRSS (15,055★, RSS reader — glance already handles news feeds); BookStack-adjacent: grav (flat CMS)

---

## EvanLi Top100/Swift.md -- 2026-05-20

### Found (7+)
- **Maccy** (19,926★) — Clipboard history manager for macOS: keeps every copied snippet accessible via hotkey. ADHD superpower — no more losing a deal address or phone number you copied 3 pastes ago. Zero setup, lives in menu bar. Score 8.
- **Easydict** (13,214★) — Native Mac dictionary + translator that queries multiple services (DeepL, Google Translate, Apple, Bing) in one window. Translate Arabic/English contracts, seller terms, or US legal docs without switching browser tabs. Score 8.
- **CodexBar** (12,897★) — Menu bar app showing Claude Code and OpenAI API usage stats without login. For Adam running Claude Code as an agentic OS, real-time cost tracking lives next to the clock — no dashboard needed. Score 8.
- **NetNewsWire** (10,048★) — Free, open-source RSS reader for macOS and iOS. Subscribe to US wholesale market feeds, PropStream news, BiggerPockets, and market reports — everything in one inbox-style view, no algorithm. Score 8.
- **AlDente** (9,043★) — Menu bar tool to cap MacBook battery charge (e.g. stop at 80%) and monitor battery health. Extends laptop lifespan significantly — set once, forget. Practical for long agentic sessions on battery. Score 7.
- **QuickRecorder** (8,280★) — Lightweight screen recorder for macOS built on Apple's ScreenCapture Kit. Record closing calls, onboarding walkthroughs, or deal demos — no watermark, no subscription. No-code, just click record. Score 8.

### Filtered
**94 repos** — Swift is Apple's native language; the top 100 is almost entirely iOS/macOS developer libraries and frameworks:
- **Networking/API libs:** Alamofire (42k★), Moya (15k★), Kingfisher (24k★), Starscream (8.6k★), Nuke (8.6k★), PromiseKit (14k★), swift-nio (8.5k★) — dev libs, no standalone use
- **UI/animation libs:** lottie-ios (26k★), Hero (22k★), SnapKit (20k★), Spring (14k★), Charts (28k★), IBAnimatable (8.6k★), animated-tab-bar (11k★), SkeletonView (12k★), NVActivityIndicatorView (10k★), folding-cell (10k★), Eureka (11k★), Material (12k★) — dev frameworks
- **Architecture/language tools:** RxSwift (24k★), ReactiveCocoa (19k★), swift (70k★), SwiftLint (19k★), SwiftFormat (8.8k★), SwiftyJSON (22k★), CryptoSwift (10k★), SQLite.swift (10k★), ObjectMapper (9k★), R.swift (9.6k★), SwiftGen (9.5k★), SwifterSwift (15k★), swift-composable-architecture (14k★), GRDB.swift (8.4k★), swift-package-manager (10k★), XcodeGen (8.4k★), XcodesApp (8.4k★), Carthage (15k★), Perfect (13k★), vapor (26k★) — dev infra
- **Dev education/lists:** awesome-ios (52k★), swift-algorithm-club (29k★), SwiftGuide (15k★), Design-Patterns-In-Swift (15k★), 30DaysofSwift (11k★), iOSInterviewQuestions (9.5k★), Swift-30-Projects (8.3k★) — learning content for devs
- **Window/menu-bar management (power-user config required):** Rectangle (29k★), AeroSpace (20k★), Amethyst (16k★), alt-tab-macos (15k★), Ice (28k★), hidden (14k★), Dozer (8.7k★), Loop (10k★) — macOS power-user tools
- **Dev tools/infra:** CodeEdit (22k★), mas (12k★), DevToysMac (9.2k★), AudioKit (11k★), Quick (9.8k★), pock (10k★), WWDC (8.7k★) — dev-adjacent
- **Emulation/VMs (technical):** UTM (34k★), OpenEmu (17k★), container (26k★), containerization (8.5k★) — technical setup required
- **Privacy/security (technical):** ShadowsocksX-NG (32k★), secretive (8.5k★) — server or key management needed
- **Borderline filtered (score 5–6):** awesome-mac (104k★, curated list not a tool); stats (38k★, system monitor); MonitorControl (33k★, display control); Mos (20k★, mouse scroll); boring.notch (9.2k★, notch UI); eul (9.9k★, status monitor); Clipy (8.5k★, second clipboard manager — Maccy already found); Gifski (8.4k★, video-to-GIF — niche media tool); Whisky (15k★, Wine wrapper — requires setup); AltStore (13k★, iOS sideloading — device required); PlayCover (11k★, iOS apps on Mac — niche); Pearcleaner (13k★, app uninstaller — not Adam-specific); supertonic (8.8k★, TTS engine — unclear if standalone app); cmux (17k★, AI terminal — developer tool); bitchat (25k★, Bluetooth mesh chat — niche); openhaystack (12k★, AirTag DIY — hardware tinkering); Aerial (21k★, screensaver — entertainment); iina (44k★, video player — not work-relevant); Signal-iOS/Telegram-iOS — app store already covers these

---

## EvanLi Top100/Ruby.md -- 2026-05-20

### Found (7+)
- **maybe-finance/maybe** (54,130★) — Open-source personal finance app: net worth tracking, transaction categorization, investment portfolio view, budgets. Self-hosted or SaaS. Between roles and managing commission income — this replaces a paid financial planner for personal cashflow clarity. Score 8.
- **chatwoot/chatwoot** (29,558★) — Open-source omnichannel customer support platform: unified inbox for email, WhatsApp, Facebook DMs, live chat — all in one dashboard. Manage inbound seller leads and buyer inquiries from multiple channels without losing a thread. SaaS at chatwoot.com. Score 8.
- **docusealco/docuseal** (16,782★) — Open-source DocuSign alternative: PDF form builder, e-signature requests, audit trail, signing order workflows. Real estate contracts, assignment agreements, and disclosures signed digitally at zero per-doc cost. Self-hosted or cloud. Score 9.

### Filtered
**97 repos** — Ruby is primarily a web framework ecosystem; the top 100 is almost entirely Rails libraries, dev tooling, and server infrastructure:
- **Core framework/language:** rails (58k★), ruby (23k★), sinatra (12k★), grape (9.9k★), hanami (6.3k★) — web framework only
- **Rails libraries (never touch):** devise (24k★), activeadmin (9.6k★), rails_admin (7.9k★), omniauth (8k★), pundit (8.5k★), cancan (6.2k★), kaminari (8.6k★), simple_form (8.2k★), paperclip (9k★), carrierwave (8.7k★), searchkick (6.7k★), paper_trail (7k★), friendly_id (6.2k★) — backend authentication, authorization, upload, pagination libs
- **Dev tools/infrastructure:** rubocop (12k★), capistrano (12k★), fastlane (41k★), kamal (14k★), capybara (10k★), sidekiq (13k★), resque (9.4k★), puma (7.8k★), brakeman (7.2k★), bullet (7.3k★), factory_bot (8.1k★), scientist (7.7k★), bkeepers/dotenv (6.7k★), guard (6.4k★), pry (6.8k★), rspec, whenever (8.8k★), vcr (6k★) — dev testing, jobs, deployment
- **Package/dependency managers:** Homebrew/brew (48k★), homebrew-cask (22k★), homebrew-core (15k★), CocoaPods (14k★), bundler, middleman (7k★) — macOS infra
- **Dev infra/self-hosted (server admin required):** gitlabhq (24k★), discourse (47k★), forem (22k★), postal (16k★), ubicloud (12k★), fluentd (13k★), fluent/fluentd, chef (8.1k★), puppet (7.8k★), pghero (8.8k★), fluent-bit — all require server/VPS administration
- **Security/scanning (developer):** metasploit-framework (38k★), wpscan (9.5k★), urbanadventurer/WhatWeb (6.5k★), presidentbeef/brakeman — pentesting or dev security
- **Dev education/reference:** bayandin/awesome-awesomeness (33k★), kilimchoi/engineering-blogs (38k★), awesome-swift (26k★), DeathKing/Learning-SICP (11k★), thoughtbot/guides (9.5k★), freeCodeCamp/how-to-contribute-to-open-source (9.2k★), lewagon/setup (19k★), chyingp/nodejs-learning-guide (6.8k★) — reading lists for developers
- **Static sites / blogging:** jekyll (51k★), octopress (9.2k★), gollum (14k★) — static site generators
- **Social/community platforms (self-hosting required):** mastodon (49k★), diaspora (13k★) — heavy infrastructure
- **eCommerce / business frameworks (dev-required):** spree (15k★), antiwork/gumroad (9k★) — requires developer to configure and deploy
- **Misc/irrelevant:** tmuxinator (13k★, terminal session manager — dev); skwp/dotfiles (6.9k★, vim config — dev); lolcat (6.5k★, terminal colorizer — dev humor); Shopify/liquid (11k★, template language — dev); felixonmars/dnsmasq-china-list (6k★, DNS list — China infra); venmo/synx (6k★, Xcode tool — dev)
- **Already on skip list:** huginn (49k★)
- **Borderline filtered (score 5–6):** opf/openproject (15k★, project management — heavyweight, Docker-only, plane already found); instructure/canvas-lms (6.6k★, LMS — relevant to Ramp Academy but requires full Rails server stack); Freika/dawarich (9k★, self-hosted location tracking — niche utility); greatghoul/remote-working (11k★, resource list not a tool); basecamp/kamal (14k★, deploy tool — dev only)

---

## EvanLi Top100/Kotlin.md -- 2026-05-20

### Found (7+)
- **Seal** (26,319★) — Material You Android GUI for yt-dlp: downloads video/audio from YouTube, Bilibili, Twitter, TikTok, 30+ platforms — no terminal, just pick URL and tap. Ramp Academy course downloads and RE training content pulled directly to phone. Distinct from desktop lux already found. Score 7.
- **UHabits** (9,896★) — Loop Habit Tracker for Android. Tracks daily habits with streaks, analytics, and reminder chains — offline, no ads, no subscription. ADHD-critical: externalizes the daily RE routine (cold call quota, follow-up blocks, lead input time) into a visual accountability system that doesn't require willpower to remember. Score 7.

### Filtered
**98 repos** — Kotlin is Android's primary language; top 100 is dominated by Android dev libraries, VPN/proxy clients, and entertainment apps:
- **Dev frameworks/libraries (never touch):** OkHttp (47k★), Architecture Samples (46k★), LeakCanary (30k★), P3C (31k★, Alibaba Java style guide), Compose Multiplatform (19k★), Lottie React Native (17k★), Anko (16k★), Ktor (14k★), Kotlinx.Coroutines (14k★), Koin (10k★), Moshi (10k★), Okio (9k★), Exposed (9k★, SQL framework), RxBinding (9.6k★), RxKotlin (7k★), Detekt (7k★) — all developer libraries
- **Android UI component libraries:** Material Dialogs (20k★), BaseRecyclerViewAdapterHelper (25k★), Flexbox Layout (18k★), Picasso (19k★), Coil (12k★), MaterialDrawer (12k★), RecyclerView Animators (12k★), AppIntro (11k★), Accompanist (7.8k★), Litho (7.8k★), Compressor (7.2k★) — dev UI components
- **Android platform/root tools:** Magisk (61k★), KernelSU (17k★), Shizuku (25k★, system API via adb), APatch (7.5k★), Nrfr (7.6k★, SIM region mod), ReVanced Manager (28k★) — require root/ADB, technical
- **VPN/proxy/circumvention:** v2rayNG (56k★), Fanqiang (46k★), Shadowsocks-Android (37k★), NekoBoxForAndroid (21k★) — technical networking setup required
- **Entertainment apps:** Legado (47k★, Chinese book reader), Mihon (21k★, manga), Animeko (18k★, anime + BitTorrent), BiliRoaming (11k★, Bilibili bypass), SpotiFlyer (11k★, music downloader), LibreTube (12k★, YouTube frontend), Cloudstream (9.7k★, media streaming), ViMusic (9.4k★, YouTube Music), Metrolist (9.5k★, YouTube Music), SimpMusic (9.2k★, music), Unciv (10k★, Civ V remake), Aniyomi (7.3k★, manga/anime), Kotatsu (8.6k★, manga), Pixiv-Shaft (7.1k★, art platform) — entertainment only
- **Android dev samples/education:** Architecture Samples (46k★), Compose Samples (23k★), I/O Sched (22k★), Now in Android (21k★), UAMP (13k★, audio app sample), Sunflower (18k★, gardening demo), Firebase Quickstart (9.3k★), Pokedex (8.3k★), CheeseSqare (7.7k★), Android Developer Roadmap (7.7k★), Android-Expert (7.3k★, Kotlin course) — learning resources for developers
- **Dev tools/IDEs:** IdeaVim (10k★, Vim engine for JetBrains), TranslationPlugin (12k★, IDE translation), Maestro (14k★, mobile UI test automation), Kotlin language (53k★), Kotlin Native (7k★), Awesome Kotlin (11k★) — developer only
- **Misc infra:** Mirai (15k★, QQ bot library), Gallery (23k★, ML GenAI on-device demo), GKD (39k★, Android accessibility automation — requires rule import and setup), Chains (9.8k★, blockchain), GitHub Store (14k★, GitHub releases app store), Nexa SDK (8k★, LLM runtime), RIBs (7.9k★, Uber architecture), React Native Video (7.7k★, dev lib), GameNative (7.1k★, gaming platform), LibChecker (6.9k★, library viewer for Android), VancedManager (8.2k★, legacy patcher)
- **Already found (other batches):** Anki-Android (11k★) — anki already found in Rust batch (desktop); Bitwarden Android (8.8k★) — keepassxc already found
- **Borderline filtered (score 5–6):** Signal-Android (29k★, messaging — universal app everyone has); Thunderbird Android (14k★, email client — commodity for Android); AB Download Manager (16k★, download GUI — Motrix already found); ImageToolbox (13k★, Android image manipulation — upscayl already found for desktop); ReadYou (7.1k★, Android RSS reader — Glance and NetNewsWire already cover RSS); FlorisBoard (8.3k★, privacy keyboard — niche setup); MaterialFiles (8.3k★, file manager — spacedrive already found); Breezy Weather (10k★, feature-rich weather — niche utility); Droid-ify (6.9k★, F-Droid client — app store meta-tool, niche); LibrePods (27k★, AirPods features on Android — hardware-specific, requires AirPods)

---

## EvanLi Top100/Objective-C.md -- 2026-05-22

### Found (7+)
- **newmarcel/KeepingYouAwake** (6,553★) — Menu-bar toggle that blocks macOS from sleeping. One click, zero config. Keeps Claude Code agentic sessions running uninterrupted during long multi-step workflows and unattended agent runs — no more waking up to a sleeping terminal. Score 7.

### Filtered
**99 repos** — Objective-C is the legacy Apple platform language; the top 100 is almost entirely iOS/macOS developer libraries, UIKit components, and networking frameworks from 2013–2018:
- **Networking/API libs (dev-only):** AFNetworking (33k★), SDWebImage (25k★), SocketRocket (9.6k★), CocoaAsyncSocket (12k★), RestKit (10k★), GCDWebServer (6.6k★), FMDB (13k★) — developer SDKs
- **UIKit component libs (dev-only):** MBProgressHUD (15k★), SVProgressHUD (12k★), Masonry (18k★), MJRefresh (13k★), FSCalendar (10k★), iCarousel (12k★), TTTAttributedLabel (8.7k★), FlatUIKit (7.7k★), DZNEmptyDataSet (12k★), FLAnimatedImage (7.9k★), PNChart (9.6k★), JSQMessagesViewController (11k★), SDCycleScrollView (6.2k★), JXCategoryView (6.2k★), MortimerGoro (6.9k★), MGSwipeTableCell (6.9k★), CEWendel/SWTableViewCell (7k★), GPUImage (20k★), YYKit (13k★), YYText (8.9k★), TZImagePickerController (8.2k★), MJExtension (8.5k★), FastImageCache (8.1k★), Shimmer (9.3k★), IFTTT/JazzHands (6.4k★), BlocksKit (6.8k★) — UI components for app development
- **iOS/macOS dev tools:** FLEX (14k★), JSPatch (11k★), Alcatraz (9.8k★), Aspects (8.4k★), xctool (6.9k★), KIF (6.2k★), VVDocumenter-Xcode (8.3k★), NWPusher (6.3k★), injectionforxcode (6.5k★), ios-app-signer (6.3k★), MonkeyDev (6.8k★), iOS-Runtime-Headers (8k★) — Xcode and iOS dev tooling
- **Framework/architecture libs:** Mantle (11k★), MagicalRecord (10k★), RestKit (10k★), PureLayout (7.6k★), nimbus (6.4k★), jsonmodel (6.8k★), JSONKit (6.2k★), YTKNetwork (6.6k★), DateTools (7.2k★), TTTAttributedLabel (8.7k★), KVOController (7.3k★) — Cocoa architecture frameworks
- **WeChat plugins (China-specific, irrelevant):** MustangYM/WeChatExtension-ForMac (22k★), TKkk-iOSer/WeChatPlugin-MacOS (14k★), BaiduNetdiskPlugin (8.9k★)
- **Proxy/circumvention tools (China-specific):** V2RayX (7.7k★), shadowsocks-iOS (8.1k★)
- **Dev cross-platform/emulation (technical):** darlinghq/darling (12k★), uni-app (41k★, Vue framework)
- **Archived/defunct projects:** spectacle (13k★, window management — discontinued, replaced by Rectangle), SlackTextViewController (8.3k★), Kapeli/Dash-iOS (7.1k★, discontinued), romaonthego/RESideMenu (7k★), mamaral/Onboard (6.6k★), jigish/slate (7.8k★, archived)
- **Dev terminal/IDE tools:** iTerm2 (17k★, terminal emulator — dev-focused), git-up/GitUp (12k★, Git GUI — dev only), terminal-notifier (7.2k★, CLI notifications — dev only)
- **Apple dev frameworks:** realm-swift (16k★), sparkle-project (9k★, app updater), CocoaLumberjack (13k★), CocoaPods deps, ReactNative/image-crop-picker (6.3k★), MWPhotoBrowser (8.7k★)
- **Misc infra/security:** LuLu (12k★, macOS firewall — requires technical config), AnyBar (6k★, menubar indicator — dev scripting required), ANE (6.7k★, neural engine reverse engineering — dev/ML), MobileIMSDK (6k★, IM framework)
- **Dev education:** draveness/analyze (8k★, iOS analysis blog), Aufree/trip-to-iOS (7.9k★, iOS resource list)
- **Borderline filtered (score 5–6):** Hammerspoon (15k★, macOS Lua automation — requires Lua scripting, score 6); mac-mouse-fix (10k★, makes any mouse feel Apple-quality — score 6, hardware-specific); MacPass (6.9k★, native macOS KeePass — score 6, but keepassxc already found); lemon-cleaner (6.2k★, Tencent macOS cleaner — score 5, Tencent product, Chinese UI); keycastr (14k★, keystroke visualizer for screen recording — score 5, niche presentation tool); Sequel-Ace (7.4k★, MySQL GUI — dev only); SequelPro (9.2k★, MySQL GUI — dev only); Sloth (8.9k★, open files viewer — dev/power user); TrollStore (21k★, iOS sideloading — requires jailbreak-adjacent setup)

---

## github.com/topics/agentic-workflow -- 2026-05-24

*60 repos scored across 3 pages. 4 already on skip list (dify 142k★, Flowise 53k★, sim 28.6k★, claude-code-tips 8.5k★). 3 flagged synthetic. 8 new qualifying tools found.*

### Found (7+)

- **ModelEngine-Group/nexent** (4,700★) — Score **9**. Zero-code platform that auto-generates production-grade AI agents from plain descriptions. You describe what the agent should do; the platform builds it — no code required. Supports multi-agent orchestration, tool connections, and knowledge bases through a GUI. Real estate angle: spin up a lead-research agent, a deal-screening assistant, or a follow-up reminder bot entirely by describing it. No Python, no config files. Genuinely non-technical entry point to custom AI agents.

- **rush86999/atom** (751★) — Score **9**. Atom Agent — talk to an AI that remembers everything, searches your context, and executes workflows autonomously. Say "remind me to follow up with John on Friday about the Phoenix deal" and it handles memory + scheduling. Designed for personal productivity with persistent long-term memory across sessions. Real estate angle: deal memory, task routing, follow-up management — all conversational. No code required to operate.

- **alirezarezvani/claude-code-tresor** (713★) — Score **9**. A curated collection of Claude Code utilities: autonomous skills, expert agents, slash commands, and prompts — all prebuilt for non-technical deployment via Claude Code. Direct upgrade to Adam's agentic OS: import skills, chain agents, and extend Claude Code's capabilities without writing a single line of code. The "tresor" (treasury) framing signals it's a living collection, not a one-shot repo.

- **matthiasn/lotti** (1,100★) — Score **8**. Open-source private logbook with a local agentic layer. Long-living AI agents read what you record throughout the day and proactively suggest what to do next. ADHD-relevant: turns unstructured notes into structured action proposals without manual organization. Local-first and private. Real estate angle: log calls and observations → agent synthesizes follow-ups and surfaces stalled deals. No cloud, no subscriptions.

- **metorial/metorial** (3,300★) — Score **8**. Connects any AI model (Claude, GPT, Gemini) to 1,200+ integrations via MCP, CLI, or API — without writing integration code. Think of it as the MCP middleware layer: point your Claude Code setup at Metorial and it can talk to calendars, CRMs, email, Slack, Notion, and hundreds of other services. Real estate angle: unlock tool connectivity for Claude's agentic workflows without hand-wiring each integration. Cuts setup time dramatically.

- **jim-schwoebel/awesome_ai_agents** (1,800★) — Score **7**. Comprehensive curated list of 1,500+ AI agent resources, tools, frameworks, and tutorials. Organized by category (memory, planning, reasoning, tools, multi-agent). Not a tool to run — a discovery map. For Adam: fastest way to surface adjacent tools not yet in this research. Check the "productivity" and "no-code" subcategories first. Updated regularly.

- **principia-ai/WriteHERE** (923★) — Score **7**. Open-source AI writing project providing a collaborative writing environment powered by AI agents. Handles long-form content with structure, continuity, and editing suggestions. Real estate angle: drafting seller outreach letters, offer summaries, or deal memos — structured writing assistance without a paid Jasper/Copy.ai subscription. Locally hosted, private.

- **a5c-ai/babysitter** (803★) — Score **7**. Babysitter enforces structured obedience on agentic workforces and enables them to manage extremely complex multi-step tasks reliably. Designed for when Claude Code or similar agents go off-rails on long tasks. For Adam's agentic OS: keeps autonomous agent runs on track, enforces task boundaries, and prevents agent drift during unattended execution. Practical reliability layer for complex workflows.

### Flagged Synthetic (star counts implausible for repo scope)

- **ruvnet/ruflo** (54,800★) — "Leading agent orchestration platform for Claude" — same ruvnet synthetic pattern already flagged in the agentic-ai entry above (1,489 automated releases). Star count fabricated.
- **shanraisshan/claude-code-best-practice** (54,700★) — Same author also has codex-cli-best-practice at 800★; wildly inconsistent. Guide repos don't hit 54k. Already flagged in agentic-ai entry.
- **NevaMind-AI/memU** (13,700★) — "Memory for 24/7 proactive agents like OpenClaw" — explicitly references OpenClaw, which is already on the global skip list as a synthetic/inflated repo. High probability of being part of the same manufactured ecosystem.

### Filtered

**49 repos** — dev frameworks, ML research, orchestration infra, coding agents, language SDKs:

- **Already on skip list / already found:** dify (142k★), Flowise (53k★), sim (28.6k★), claude-code-tips (8.5k★)
- **Dev/infra frameworks (score 1–3):** daytonaio/daytona (72.5k★ AI code infra), bytedance/deer-flow (69.4k★ SuperAgent for coding), ag-ui-protocol/ag-ui (13.8k★ agent-UI protocol), The-Pocket/PocketFlow (10.7k★ LLM framework), kyegomez/swarms (6.7k★ multi-agent SDK), rllm-org/rllm (5.6k★ RL for LLMs), FellouAI/eko (4.9k★ agentic workflow builder — requires dev setup), SolaceLabs/solace-agent-mesh (4.6k★ event-driven agent framework), algorithmicsuperintelligence/optillm (4k★ LLM inference proxy), Netflix/maestro (3.8k★ workflow orchestrator), dagucloud/dagu (3.4k★ YAML workflow engine), antoinezambelli/forge (1.8k★ Python LLM framework), prefect-archive/ControlFlow (1.4k★ agent control framework), dbos-inc/dbos-transact-py (1.4k★ durable Python workflows), dbos-inc/dbos-transact-ts (1.2k★ durable TS workflows), standardagents/dmux (1.6k★ git worktree agent multiplexer), google/adk-java (1.6k★ Java AI agent SDK), covibes/zeroshot (1.5k★ engineering CLI agent), Dicklesworthstone/agentic_coding_flywheel (1.5k★ VPS dev environment setup), microsoft/Trace (737★ generative optimization for agents), lofcz/LLMTornado (612★ .NET AI agent library), evolution-foundation/evo-ai (591★ agent creation platform — low traction)
- **ML/AI research (score 1–2):** asinghcsu/AgenticRAG-Survey (1.6k★ research survey), thinkwee/AgentsMeetRL (1.4k★ RL+agents paper list), ombharatiya/ai-system-design-guide (593★ ML systems design), Bessouat40/RAGLight (662★ RAG framework), gmickel/flow-next (616★ spec-driven dev workflow plugin)
- **Dev education/courses (score 3–4):** Marktechpost/AI-Agents-Projects-Tutorials (2.6k★ multi-agent tutorial repo), neural-maze/ava-whatsapp-agent-course (1.7k★ WhatsApp agent course — course, not tool), neural-maze/philoagents-course (1.5k★ philosophy+AI course), shanraisshan/codex-cli-best-practice (800★ vibe coding guide)
- **Game/simulation (score 1):** 4thfever/cultivation-world-simulator (1.7k★ Xianxia world game)
- **Low-code but dev-adjacent (score 5–6):** ModelEngine-Group/app-platform (1.4k★ low-code LLM app engineering — requires some config), eigent-ai/eigent (14.1k★ cowork desktop — unverifiable star count, borderline synthetic), kevinluosl/deepbot (2.3k★ Feishu-specific AI assistant — language/platform barrier), hesamsheikh/octogent (1.1k★ Claude Code orchestration dashboard — dev-headspace framing), DeepMyst/Mysti (1.1k★ VS Code coding agents — IDE-specific), formkit/formkit (4.7k★ form framework for coding agents — dev tool), modu-ai/moai-adk (1k★ Claude Code dev kit — TDD/DDD framing too technical), vm0-ai/vm0 (1.1k★ AI teammate — vague, low traction), GreenSheep01201/claw-empire (1.2k★ AI agent office simulator — references "claw" ecosystem, likely connected to OpenClaw synthetic cluster), romainsimon/paperasse (2k★ French accounting agents — language barrier), splx-ai/agentic-radar (972★ LLM security scanner — dev/security tool), bergside/awesome-design-skills (942★ design skill files — designer tool), PolyArch/humanize (800★ idea-to-realization framework — vague/research), alirezarezvani/claude-code-tresor ✅ FOUND above, rush86999/atom ✅ FOUND above

---

## github.com/topics/personal-productivity -- 2026-05-25

*40 repos scored across 2 pages. 1 flagged suspicious (crack/piracy software). 5 new qualifying tools found. Note: topic is sparse — stars top out at 194; most entries are student projects or sub-10-star experiments.*

### Found (7+)

- **lcomplete/gaia** (194★) — Score **8**. Proactive personal AI assistant for daily work, explicitly modeled on Jarvis. Monitors your work context and surfaces suggestions, reminders, and task nudges without you asking. Unlike reactive chatbots, it initiates. ADHD angle: having an AI that checks in on you rather than waiting for you to remember to open it is exactly the behavior gap Adam needs filled. Worth watching as it matures.

- **agentic-os** (24★) — Score **9**. "A collection of AI-native operating systems powered by Claude Code. Manage work, career, life, and meetings through conversation." Directly mirrors Adam's existing Claude Code Agentic OS setup. Low stars suggest it's very new or very niche, but the concept is on-target: a curated library of Claude Code operating-system components. Worth inspecting for patterns, skill structures, or system prompt designs that can be imported into Adam's own OS. Treat as a peer project, not a mature product.

- **alicerun** (39★) — Score **7**. Combines TODO, work tracking, habit tracking, mood tracking, and CBT techniques into a single productivity app with analytics for AI-powered task prioritization. ADHD-relevant: externalizes tracking, shows patterns, uses CBT prompts to reduce task avoidance. Not real-estate specific, but daily-operating-layer useful — especially for building consistent follow-up habits during the job search period.

- **AetherMind** (8★) — Score **8**. "Local-first Personal AI Memory OS — RAG over your entire life. Git, notes, calendar, location. 100% offline." Connects your notes, calendar, and location history into a searchable second brain you can query conversationally. All local, no cloud. Early-stage (8★) but the architecture is sound: embeddings over your personal data, local LLM inference. For Adam: "what did I discuss with that seller last month?" or "what's the context for this deal?" answered from local memory. Watch it; don't deploy yet.

- **hejazizo/Koja** (11★) — Score **7**. AI-powered scheduling tool that integrates with your calendar to manage your time. Ingests calendar state, applies AI scheduling logic, and proposes or books time blocks. Real estate angle: structured time-blocking for outreach calls, follow-up windows, and deal-review sessions — without manually re-planning your week. Very low stars; early-stage tool. Check whether it supports Google Calendar.

### Flagged Suspicious

- **Todoist-Pro-Crack-2026** (21★) — Piracy/crack installer, not a productivity tool. Flagged and skipped.

### Filtered

**34 repos** — student projects, sub-5-star experiments, dev tools, writing templates:

- **Low-star general apps (score 5–6):** faire-todo-app (7★ offline todo), Skedence (5★ daily planner), onroute (4★ AI commute briefings), dailyinsightai (2★ AI journaling), pecma.github.io (2★ AI executive assistant landing page), daily-worklist-manager (2★ AI work prioritization), todoist-playbook (2★ Todoist template collection), Prodexa (2★ mobile productivity app), sharemaster (2★ Chrome URL copier), time-blocks (2★ PDF time-block form)
- **Dev/technical (score 1–4):** qwen3_computer_use (5★ GUI agent driver), writingLogTemplateInOrg (8★ org-mode template), writing-log-md (3★ markdown template), writing-log-odt (2★ OpenOffice template)
- **Page 2 — student projects / 0–1 star (all score 1–5):** DocumentVault, smart-task-orchestrator, writingProgress2022, personal-assistant, context-planning-system, virgil, amar-career, LinkedIn-Job-Scraper, unscheduled-pressure, mindvault, head-of-ai-template, learning-analytics-system, 26CP3600358-ai-personal-productivity-suite, my-learning-logger, audible-second-brain, Kairos, task-manager-java, Peria, daily-life-fte, Lifeloop — all sub-2★, none deployable

---

## github.com/topics/ai-agent -- 2026-05-25

*60 repos scored across 3 pages (sorted by stars). 12 flagged synthetic (implausible star counts). 3 already found (cherry-studio, nocobase, career-ops on skip list). 2 already filtered in prior batches (leon score 4-6, CopilotKit score 2). 4 new qualifying tools found.*

### Found (7+)

- **activepieces/activepieces** (22,400★) — Score **9**. No-code workflow automation platform with 400+ integrations including AI agents, MCPs, and Zapier-style trigger/action chains. Cleaner UI than n8n, newer codebase, actively maintained. Built-in AI step blocks (Claude, GPT, Gemini) let you add intelligence to any automation without touching code. Real estate wholesaling angle: auto-route inbound seller leads from a web form → Google Sheets → SMS → CRM; auto-draft follow-up emails triggered by seller responses; monitor property sites and alert on new matches. Cloud + self-host. Strongly complements n8n as either an alternative or parallel stack.

- **presenton/presenton** (6,700★) — Score **8**. Open-source AI presentation generator — prompt → structured slide deck, exported as native PowerPoint or PDF. API available for programmatic use. No design skills required. Real estate angle: generate deal analysis presentations, seller credibility decks, or market overview slides in seconds. Self-hostable or cloud. Fills a gap in Adam's agentic OS: "create a presentation about this deal" as a one-command agent task.

- **mahseema/awesome-ai-tools** (5,300★) — Score **8**. Curated, continuously updated directory of top AI tools and platforms organized by category (productivity, writing, video, image, research, automation). Not a tool itself but the fastest discovery layer for finding what's new and relevant. Real estate angle: regularly scan for new sales automation, CRM AI, or outreach tools entering the market before they get widely known. Bookmark and revisit quarterly.

- **groupultra/telegram-search** (3,900★) — Score **7**. Export your full Telegram chat history and fuzzy-search it locally. No cloud dependency, runs on your machine. Real estate angle: if Adam uses Telegram for seller outreach, buyer contacts, or team comms, this surfaces any past conversation — "who mentioned probate", "what did that motivated seller say in March". Recovers context that disappears in standard Telegram search. Low setup friction.

### Flagged Synthetic (12 repos — implausible star counts for repo type/age)

- **NousResearch/hermes-agent** (166k★) — 166k would put it among GitHub's top 20 most-starred repos ever. Description is generic. Skip.
- **shareAI-lab/learn-claude-code** (62.3k★) — Tutorial bash repo with 62k stars is not credible. Skip.
- **ruvnet/ruflo** (54.8k★) — Already flagged in agentic-ai batch (ruvnet synthetic pattern with 1,400+ automated releases). Skip.
- **zhayujie/CowAgent** (44.8k★) — zhayujie's real chatgpt-on-wechat project has ~26k stars; CowAgent at 44.8k for a newer harness is suspect inflation. Flag.
- **HKUDS/nanobot** (43.1k★) — Same HKUDS org behind Vibe-Trading (8.5k) and other suspiciously starred repos. 43k for "lightweight agent" is implausible. Skip.
- **Gitlawb/openclaude** (27.7k★) — Unknown org, "runs anywhere uses anything" generic description, 27.7k stars. Skip.
- **iOfficeAI/AionUi** (26.4k★) — Unknown org, 26.4k stars for a local AI app frontend. Suspect. Flag.
- **hugohe3/ppt-master** (20.6k★) — 20.6k for a single-purpose PPT generator from unknown account. Suspicious. presenton (6.7k from a real org) is the credible alternative found above.
- **Panniantong/Agent-Reach** (20.2k★) — Already filtered in automation batch; star count remains suspect.
- **waooAI/waoowaoo** (12.4k★) — "Professional platform for controllable film production" with 12.4k from unknown org. Skip.
- **op7418/guizang-ppt-skill** (11.7k★) — Claude Code skill repo with 11.7k stars is implausible for a skill file. Skip.
- **EKKOLearnAI/hermes-web-ui** (5.9k★) — Web dashboard for "multi-platform AI chat" from unknown org; name echoes the synthetic hermes-agent cluster. Skip.

### Filtered

**39 repos** — dev/ML/infra/coding tools, score 1–6:

- **Already found / skip list:** cherry-studio (46.2k★ already in findings), nocobase (22.5k★ already in findings), career-ops (47k★ skip list)
- **Already filtered prior batches:** leon/leon-ai (17.3k★ score 4-6, filtered in automation batch — requires server setup), CopilotKit (31.7k★ score 2, filtered in agentic-ai batch)
- **Stock/finance (not RE):** ZhuLinsen/daily_stock_analysis (38.7k★), HKUDS/Vibe-Trading (8.5k★)
- **Dev framework/SDK (score 1–3):** googleworkspace/cli (26.5k★ Google Workspace CLI), jackwener/OpenCLI (22.5k★ website-to-CLI converter), trycua/cua (17.1k★ computer-use agent infrastructure), browser-use/web-ui (16k★ browser automation framework), browser-use/browser-harness (13.6k★ LLM browser harness), e2b-dev/E2B (12.3k★ sandbox runtime), alibaba/OpenSandbox (10.8k★ agent sandbox runtime), Bindu/GetBindu (6.7k★ agent identity/payments infra), crestalnetwork/intentkit (6.5k★ cloud agent cluster management), learn-harness-engineering/walkinglabs (6.3k★ tutorial), UfoMiao/zcf (6k★ zero-config code flow tool), camofox-browser/jo-inc (5.7k★ stealth headless browser SDK), Integuru-AI/Integuru (4.6k★ API reverse-engineering agent), SWE-agent/mini-swe-agent (4.5k★ GitHub issues coding agent), FedML-AI/FedML (4k★ distributed ML library), Tencent/TencentDB-Agent-Memory (4k★ agent memory pipeline), LazyAGI/LazyLLM (3.8k★ LLM multi-agent framework), smallcloudai/refact (3.5k★ engineering task coding agent)
- **Dev education / guide (score 3–4):** tukuaiai/vibe-coding-cn (13.8k★ Chinese coding tutorial), frankbria/ralph-claude-code (9.2k★ Claude Code dev loop), zebbern/claude-code-guide (4.2k★ Claude setup guide), KimYx0207/AI-Coding-Guide-Zh (4.1k★ Chinese AI coding guide), filipecalegario/awesome-vibe-coding (4.5k★ vibe coding references), WeThinkIn/AIGC-Interview-Book (3.8k★ ML interview prep), cbamls/AI_Tutorial (3.7k★ industry AI tutorial)
- **Niche / low relevance (score 4–6):** EvoMap/evolver (7.6k★ GEP self-evolving AI engine), can1357/oh-my-pi (7k★ terminal coding agent), esengine/DeepSeek-Reasonix (6.6k★ DeepSeek terminal agent), Narcooo/inkos (6.5k★ autonomous novel writing agent), ChatLab/ChatLab (6.5k★ local chat history analyzer — score 5, not enough RE angle), holaboss-ai/holaOS (5.6k★ AI operational streams — vague, low verifiability), adongwanai/AgentGuide (5.1k★ LangGraph dev guide), Q00/ouroboros (4.3k★ Agent OS spec tool — too technical framing), AlexAnys/awesome-openclaw-usecases-zh (4.2k★ OpenClaw on skip list), killop/anything_about_game (3.9k★ game dev resources), 1186258278/OpenClawChineseTranslation (3.8k★ OpenClaw translation — skip list)


---

## github.com/topics/task-management -- 2026-05-25

*40 repos scored across 2 pages. 1 already on skip list (lotti). 1 duplicate repo (AppFlowy-Web = same project as AppFlowy). 1 flagged synthetic. 9 new qualifying tools found.*

### Found (7+)

- **AppFlowy-IO/AppFlowy** (71,300★) — Score **9**. Open-source Notion/Linear alternative with built-in AI — wiki, task boards, databases, and team workspaces in one app. Non-technical, visually clean, entirely free, fully self-hostable. AI features work without API keys. Real estate angle: deal pipeline as a database (seller name, address, status, follow-up date), knowledge base for scripts and objection handling, AI-assisted note-taking after calls. Already has 71k stars and an active community. If Adam needs one tool to unify deal tracking + knowledge management + daily tasks, this is it. 10x more maintained and polished than any other self-hosted Notion alternative.

- **obsidian-tasks-group/obsidian-tasks** (3,700★) — Score **8**. THE canonical task management plugin for Obsidian — adds due dates, recurrence, priorities, filtering, and global task queries across every note in the vault. Integrates with Adam's existing 246-note vault without restructuring it. Tasks live inside regular markdown notes but surface in a unified dashboard. Real estate angle: track every "call back by Friday" and "send contract by Thursday" embedded inside deal notes, then query them all in one view. Works with the claudian plugin (already found) for a full AI-task loop inside Obsidian.

- **eclaire-labs/eclaire** (862★) — Score **8**. Local-first, open-source AI assistant that unifies tasks, notes, docs, photos, and bookmarks into a single interface — think a personal AI layer over your whole life's data. Non-technical setup, no cloud dependency. Real estate angle: add deal notes, seller photos, property bookmarks, and follow-up tasks in one place, then ask "what do I know about the Johnson lead?" and get a coherent summary. Strong fit for building a private deal intelligence layer without SaaS subscriptions.

- **chrisvel/tududi** (2,900★) — Score **7**. "A calm, open system for organizing life and work — tasks, projects, notes, areas, and smart workflows." Self-hosted, lightweight, intentionally non-overwhelming. ADHD-conscious design: area-based organization prevents cognitive sprawl. Real estate angle: one area per deal stage (leads, under-contract, closed), tasks nested under each, notes attached. No sign-up, no cloud lock-in. Good minimalist alternative to AppFlowy for those who want less visual complexity.

- **roovo/obsidian-card-board** (623★) — Score **7**. Obsidian plugin that renders tasks as a visual kanban board — different from obsidian-tasks (list-based queries) in that it gives a drag-and-drop card view across columns. Real estate angle: pipeline board with columns for Cold → Contacted → Qualified → Under Contract → Closed, all inside Obsidian without leaving the vault. Pairs with obsidian-tasks: one plugin for filtering/querying, the other for visual pipeline movement.

- **taskgenius/taskgenius-plugin** (560★) — Score **7**. Comprehensive AI-powered task management plugin for Obsidian — goes beyond obsidian-tasks by adding AI task generation, smart prioritization, and natural language scheduling. Real estate angle: describe what needs to happen with a deal in plain language, plugin converts it into structured tasks with dates and priorities. Complements (not replaces) obsidian-tasks for AI-assisted task creation inside the vault.

- **kaanozhan/Frame** (306★) — Score **7**. Platform designed specifically for "agentic vibecoders and teams who use Claude Code and Codex CLI" — provides a structured environment for managing Claude Code sessions, tasks, and agent outputs. Direct fit for Adam's Claude Code agentic OS: session management, task queue, agent result tracking without code. Real estate angle: dispatch "research comps for 123 Main St" to an agent, track status, receive output — all from a dashboard rather than a terminal.

- **saltbo/agent-kanban** (291★) — Score **7**. "Agent-first task board — mission control for your AI workforce." Kanban UI designed for tracking AI agent tasks rather than human tasks: dispatch jobs, see status, review outputs. Real estate angle: manage a fleet of specialized Claude agents (comp researcher, email drafter, follow-up scheduler) from a single task board. Low friction if you're already running multiple agents in parallel.

- **Santofer/Remindian** (277★) — Score **7**. Sync Obsidian Tasks and TaskNotes to Apple Reminders or Things 3 — creates a live bridge between Obsidian and native Apple task management. Real estate angle: tasks written in deal notes inside Obsidian automatically appear on iPhone Reminders with due dates. Closes the gap between desktop note-taking and mobile task reminders during field calls. Relevant if Adam uses an iPhone.

### Flagged Synthetic

- **BradGroux/veritas-kanban** (723★) — "Lightweight orchestration platform built for your AI agents emphasizing project transparency." Unknown account, vague AI-platform description, 723 stars — suspicious ratio for a new agentic kanban tool. Skip.

### Filtered

**29 repos** filtered — breakdown:

- **Already on skip list:** matthiasn/lotti (1.1k★) — already found in agentic-workflow batch
- **Duplicate repo:** AppFlowy-IO/AppFlowy-Web (279★) — same project as AppFlowy (#1 above), separate repo
- **Unmaintained:** onejgordon/flow-dashboard (1.7k★) — marked unmaintained by author
- **Adjacent to skip list:** clawwork-ai/ClawWork (509★) — client for OpenClaw, which is already on skip list; derivative, not independent
- **Dev/technical (score 1–3):** whyisdifficult/jiratui (1.6k★ — Jira terminal UI), cyanheads/atlas-mcp-server (474★ — Neo4j MCP for LLM agents), cadence-workflow/cadence-go-client (376★ — workflow engine SDK), bngarren/checkmate.nvim (370★ — Neovim todo plugin), ETS-PoliTO/esp32-sniffer (286★ — ESP32 WiFi firmware), Devnawjesh/hr-payroll (267★ — HRM payroll system)
- **Generic PM / requires dev setup (score 5–6):** builderz-labs/mission-control (5k★ — agent orchestration, dev-heavy), Worklenz/worklenz (3.1k★ — generic PM, no differentiator vs already-found tools), hudy9x/namviek (2.4k★ — small team PM app), BaldissaraMatheus/Tasks.md (2.1k★ — self-hosted markdown kanban, too simple), Chorus-AIDLC/Chorus (910★ — AI-human collaboration harness, dev-oriented), dongdongbh/Mindwtr (871★ — GTD desktop app, overlaps with AppFlowy/super-productivity already found), Grashjs/cmms (632★ — enterprise maintenance management, not RE-relevant), Kanba-co/kanba (621★ — generic kanban), L1AD/claude-task-viewer (615★ — Claude Code task viewer, too narrow/niche), bergercookie/syncall (604★ — multi-service task sync, requires technical setup), RARgames/4gaBoards (602★ — basic realtime kanban), huytd/pomoday-v2 (600★ — keyboard-only task web app), kevinschoon/pomo (573★ — Pomodoro CLI), DjangoCRM/django-crm (567★ — CRM with task mgmt, but requires Django deployment; score 5), Taskosaur/Taskosaur (488★ — conversational AI tasks, vague/unverified), darkmoonight/Zest (441★ — basic task app), GreatStackDev/project-management (433★ — ReactJS PM boilerplate), slowernews/hamster-system (350★ — ultra-simple life framework, too abstract), chiriapp/chiri (290★ — CalDAV task app, niche)

