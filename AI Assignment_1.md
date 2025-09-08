2.Yes,Yes,No,Yes,No,Yes,No,No,Yes,No

Explaination 

AI is being used in hospitals and clinics for analyzing symptoms, scans, and test data—Watson Health and K Health are real examples. These tools help doctors, but don’t replace them.

AI translation apps can handle real-time voice-to-voice translation for many languages. Some apps like DeepL and Google Translate now support spoken German and Arabic, but the quality isn’t near perfect, especially for less common language pairs or in super noisy places.

AI can make educated guesses about future trends using data, but true “future event prediction” (as in knowing the future like time travel) is impossible. There are too many unpredictable factors, and AI can’t see what hasn’t happened yet.

There are AI bots (GIB, Argine) that play bridge online and even beat human tournament champions sometimes. AI can play at a high level, though some human strategies are hard to copy.

Scientists can simulate small animal brains (like a mouse’s brain), but simulating all of the human brain’s complexity isn’t possible yet. Computing limits and our incomplete understanding of the brain make this infeasible for now.

Modern chatbots (ChatGPT, Gemini) can hold surprisingly good conversations, answer questions, and provide support for millions of users. They are a huge AI success story but aren’t perfect humans.

AI can analyze language and predict some emotional patterns or behavior, but it doesn’t have real emotions or true intuition about humans. Some new models do surprisingly well on emotional intelligence quizzes, but they don’t “understand” like humans do.

Robots and AI help in stores (stocking shelves, picking items for delivery), but an AI or robot that shops for a whole week’s groceries like a regular person—walking through aisles, choosing stuff, dealing with checkout—doesn’t really exist for everyday use yet.

Netflix, Amazon, and YouTube all use AI to recommend movies, shows, and products to individual users based on their habits. This is routine and works really well for most people.

No AI can actually “interpret” dreams in a meaningful or scientific way. At best, AI might find patterns in dream journals, but interpreting the meaning of dreams is still subjective and not something AI can do reliably.

1.

a)

My CWID ends with 8, which corresponds to the Cybersecurity category. For this assignment, I've selected two notable AI computer systems/tools in cybersecurity:

CrowdStrike Falcon Platform with Charlotte AI

Darktrace Enterprise Immune System

These are both industry-leading AI-powered cybersecurity platforms that represent the current state of artificial intelligence in cybersecurity applications.


(b) 
**CrowdStrike Falcon Platform with Charlotte AI**

The Falcon platform is a cloud-native cybersecurity solution , it runs on computers and watches for threats But it’s not like the old antivirus tools that just looked for known viruses. Instead, it tries to watch behavior and flags anything that looks weird. The Charlotte AI part is newer, and from what I could tell, it’s meant to help security analysts sort through the alerts faster and even automate some investigation steps.

Three main functions:

Autonomous Threat Detection and Prevention: Uses AI-powered behavioral analysis to identify malicious activities in real-time, including zero-day attacks, ransomware, and fileless malware without relying on signature-based detection.

Automated Incident Response and Investigation: Charlotte AI accelerates detection, performs automated investigations, and can execute response actions with bounded autonomy to contain threats before they spread.

Threat Intelligence and Hunting: Processes enormous number of events daily (in millions) through machine learning models to identify attack patterns, adversary tactics, and provide actionable intelligence for proactive threat hunting

**Darktrace Enterprise Immune System**

Darktrace's system accomplishes autonomous cyber defense by mimicking the human immune system to understand what's "normal" for an organization and detect deviations that indicate threats.
The idea is every organization behaves differently, so a one-size-fits-all approach doesn’t work.

Three main functions:

Self-Learning Behavioral Analysis: Continuously learns the "pattern of life" for every user, device, and network component to build a dynamic baseline of normal activity, enabling detection of subtle anomalies that other tools miss.

Real-time Threat Detection Across All Environments: Monitors and protects network, cloud, email, IoT, and operational technology environments simultaneously, correlating threats across multiple attack vectors.

Autonomous Response with Antigena: Takes precise, surgical actions to neutralize in-progress attacks at machine speed without disrupting normal business operations, such as slowing suspicious connections or isolating compromised devices.


(c) AI Technologies 

CrowdStrike uses,

Machine Learning for Behavioral Analysis: Uses supervised and unsupervised learning algorithms trained on threat intelligence from billions of security events to identify attack patterns and classify threats with high accuracy.

Natural Language Processing (NLP): Charlotte AI employs large language models to enable natural language querying of security data, automated report generation, and plain-language interaction with the platform.

Graph Neural Networks and Real-time Analytics: The Falcon Threat Graph processes massive datasets using graph-based analytics to map attack relationships and provide real-time threat correlation across the entire environment.

Darktrace uses,

Unsupervised Machine Learning with Bayesian Methods: Uses Bayesian probabilistic models and recursive Bayesian estimation to continuously update threat assessments and build evolving "patterns of life" without requiring labeled training data.

Clustering Algorithms and Anomaly Detection: Employs multiple clustering techniques (matrix-based, density-based, hierarchical) combined with dozens of anomaly detection models to identify deviations from normal behavior.

Graph Neural Networks (GNNs) and Recurrent Neural Networks (RNNs): The DIGEST model combines GNNs to interpret incident structure with RNNs to analyze how threats evolve over time, improving incident prioritization and scoring.


(d) Performance vs Humans

CrowdStrike

There’s no way humans can process 180 billion events per day. This can, and it also reduces false positives a lot. One example I saw was Charlotte AI filtering out the junk alerts so analysts only get the real issues. Their market share is growing, which seems like proof it’s working well.

Darktrace

The stats here were pretty eye-opening. In one study, they cut 9.6 billion events in a month down to just 54 that needed a human. That’s crazy. They also claim to reduce false positives by about 90%.

What’s interesting is that it improves over time — decent after one month, really good after a year. That makes sense because it needs to learn the environment.

(e) Real-world Usage

CrowdStrike

This is definitely not experimental. Thousands of companies use it, especially big ones. It’s global but seems most common in the U.S. Security teams mainly run it, but Charlotte AI makes it more approachable for people who aren’t hardcore experts.

Darktrace

Also widely deployed , they say 10,000+ customers worldwide. I was surprised to see it being used in hospitals, energy companies, and even manufacturing plants. Because it’s self-learning, teams don’t have to waste time writing rules, but you still need analysts who can interpret what it’s saying.

(f) What Makes These “Intelligent”

CrowdStrike Falcon

It keeps learning from new attacks, not just old signatures

Understands attack chains, not just single events

Charlotte AI can explain results in natural language (almost like a human talking you through it)

Darktrace

Self-learns normal patterns instead of being told rules

Adapts as organizations change

Antigena can make autonomous decisions to stop attacks while letting business run smoothly

(g) Technical Implementation

CrowdStrike

From job postings and tech talks, it seems they use Python, Java, C++, and even Rust in some parts. For AI, TensorFlow is a main framework. Everything’s cloud-native and containerized. They also have Falcon Foundry, which lets you build custom apps without much coding.

Darktrace

Probably heavy on Python (and maybe R) since the math is statistical. They use Bayesian models, clustering, and neural nets. Architecture wise, it’s distributed and connects through APIs.

The UI is pretty unique with a live 3D visualization of your network and threats. That feels more intuitive compared to old-school dashboards.

(h) References and Further Reading
Where I acquired application information:

Academic and Research Sources:
University of Cambridge research on Darktrace's mathematical foundations

MIT and Harvard case studies on AI in cybersecurity

Academic papers on machine learning in cybersecurity from ACM Digital Library

Industry Reports and Documentation:
CrowdStrike official technical documentation and platform guides

Darktrace technical whitepapers and product documentation

Independent analyst reports from IDC, Forrester, and Gartner

Recommended Books and Publications:
"Applying Artificial Intelligence in Cybersecurity Analytics and Cyber Threat Detection" by Shilpa Mahajan - Comprehensive coverage of AI applications in cybersecurity with practical frameworks

"AI for Cybersecurity - A Handbook of Use Cases" - Penn State Cybersecurity Lab publication providing practical examples and source code for AI security implementations

"The Language of Deception: Weaponizing Next Generation AI" by Hutchens - Explores both offensive and defensive AI applications in cybersecurity

"Defensive Security Handbook: Best Practices for Securing Infrastructure" - Second edition covering modern AI-powered security practices

Online Resources:
CrowdStrike Developer Center: https://developer.crowdstrike.com - APIs, SDKs, and integration guides

Darktrace Cyber AI Platform: Official documentation and technical resources

MITRE ATT&CK Framework: For understanding AI detection capabilities against attack techniques

OWASP Top 10 for LLMs: Essential for understanding AI security vulnerabilities

Professional Development:
ISACA AAISM™ Certification: AI Security Management certification for practitioners

ISC2 AI Security Training: Professional development courses on AI cybersecurity

Industry conferences like Fal.Con (CrowdStrike) and cybersecurity research symposiums
