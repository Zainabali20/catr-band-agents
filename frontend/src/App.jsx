import "./App.css";

function App() {
  const agents = [
    {
      step: "01",
      name: "Assessment Agent",
      role: "Extracts student profile",
      detail:
        "Reads raw student input and converts it into structured guidance context including age, country, interests, strengths, weak areas, and goals.",
    },
    {
      step: "02",
      name: "Career Mapper Agent",
      role: "Maps career tracks",
      detail:
        "Recommends primary and alternative paths based on the student profile, strengths, risks, and future opportunities.",
    },
    {
      step: "03",
      name: "Roadmap Planner Agent",
      role: "Builds localized roadmap",
      detail:
        "Creates a country-specific academic, skill, salary, and action roadmap for the selected career direction.",
    },
    {
      step: "04",
      name: "Review & Decision Agent",
      role: "Approves final plan",
      detail:
        "Reviews quality, realism, risk level, readability, and produces the final approved roadmap with modifications.",
    },
  ];

  return (
    <main className="page">
      <section className="hero">
        <div className="heroText">
          <p className="badge">Band-powered multi-agent workflow</p>

          <h1>CATR — Career Advisory Team for Students</h1>

          <p className="subtitle">
            A Pakistan-first, globally adaptable multi-agent career guidance
            system where specialized agents assess, map, plan, review, and
            approve student roadmaps through Band.
          </p>

          <div className="heroActions">
            <a href="#workflow" className="primaryBtn">
              View Workflow
            </a>
            <a href="#roadmap" className="secondaryBtn">
              Sample Roadmap
            </a>
          </div>
        </div>

        <div className="studentCard">
          <p className="cardLabel">Sample Student Profile</p>
          <h2>Kumail, 24</h2>

          <ul>
            <li>
              <strong>Country:</strong> England
            </li>
            <li>
              <strong>Interests:</strong> Space, maths, science
            </li>
            <li>
              <strong>Strong subjects:</strong> Mathematics, chemistry, science
            </li>
            <li>
              <strong>Weak areas:</strong> Urdu, English
            </li>
            <li>
              <strong>Dream job:</strong> Space scientist, engineer,
              entrepreneur
            </li>
            <li>
              <strong>Parent expectation:</strong> Stable career with good
              income
            </li>
          </ul>
        </div>
      </section>

      <section className="section" id="workflow">
        <div className="sectionHeader">
          <p className="eyebrow">Agent Collaboration</p>
          <h2>Not a single chatbot — a reviewable decision workflow</h2>

          <p>
            CATR uses Band as the collaboration layer. Each agent performs a
            separate role, passes structured context, and hands off the task to
            the next agent. This makes the process visible, reviewable, and more
            trustworthy than a one-shot chatbot answer.
          </p>
        </div>

        <div className="workflowGrid">
          {agents.map((agent) => (
            <div className="agentCard" key={agent.name}>
              <span className="step">{agent.step}</span>
              <h3>{agent.name}</h3>
              <p className="role">{agent.role}</p>
              <p>{agent.detail}</p>
            </div>
          ))}
        </div>

        <div className="handoffBox">
          <span>Live Band Handoff Flow</span>
          <code>
            Assessment → Career Mapper → Roadmap Planner → Review & Decision
          </code>
        </div>
      </section>

      <section className="section roadmapSection" id="roadmap">
        <div>
          <p className="eyebrow">Final Reviewed Output</p>
          <h2>Approved career roadmap with decision scorecard</h2>

          <p className="muted">
            This example shows CATR adapting from a Pakistan-first workflow to an
            England-specific roadmap, proving that the system can localize
            guidance for different education markets.
          </p>

          <div className="scoreCard">
            <h3>Quality Review Scorecard</h3>

            <ul>
              <li>
                Student-career fit: <strong>9/10</strong>
              </li>
              <li>
                UK relevance: <strong>9/10</strong>
              </li>
              <li>
                Academic pathway clarity: <strong>8/10</strong>
              </li>
              <li>
                Readability: <strong>9/10</strong>
              </li>
              <li>
                Risk level: <strong>Medium</strong>
              </li>
              <li>
                Final decision: <strong>APPROVED WITH MODIFICATIONS</strong>
              </li>
            </ul>
          </div>
        </div>

        <div className="roadmapCard">
          <h3>Recommended Career Paths</h3>

          <p>
            <strong>Primary path:</strong> Aerospace / Mechanical Engineering
          </p>
          <p>
            <strong>Alternative path:</strong> Data Science / AI for Space
            Applications
          </p>

          <h3>Why This Fits</h3>
          <ul>
            <li>
              Strong mathematics, chemistry, and science background supports
              technical career routes.
            </li>
            <li>
              Space interests align with aerospace engineering, space systems,
              satellite data, and AI-based research.
            </li>
            <li>
              Entrepreneurship can later connect with space-tech startups,
              satellite analytics, or engineering services.
            </li>
          </ul>

          <h3>England-Specific Academic Roadmap</h3>
          <ul>
            <li>
              Consider Aerospace Engineering, Mechanical Engineering, Physics,
              Data Science, or Space Engineering pathways.
            </li>
            <li>
              Explore foundation year, part-time, or online degree options if
              traditional A-level requirements are incomplete.
            </li>
            <li>
              Relevant options may include engineering degrees, Open University,
              FutureLearn, and postgraduate space/data science routes.
            </li>
          </ul>

          <h3>Skill Roadmap</h3>
          <ul>
            <li>Python programming for data science and automation</li>
            <li>CAD tools such as SolidWorks or AutoCAD</li>
            <li>Machine learning basics using TensorFlow or PyTorch</li>
            <li>Space data analysis using public datasets and NASA APIs</li>
            <li>Technical English or engineering communication courses</li>
          </ul>

          <h3>Modified 7-Day Action Plan</h3>
          <ul>
            <li>Day 1: Research UK aerospace and space engineering programs</li>
            <li>Day 2: Start a beginner Python course</li>
            <li>Day 3: Watch NASA or UK Space Agency public lectures</li>
            <li>Day 4: Try beginner CAD software tutorials</li>
            <li>Day 5: Build a simple GitHub project or coding portfolio</li>
            <li>Day 6: Draft a space-tech startup idea</li>
            <li>Day 7: Compare foundation year, online, and degree options</li>
          </ul>

          <h3>Disclaimer</h3>
          <p>
            This is AI-assisted guidance and should be validated with parents,
            teachers, counselors, official university admission sources, and
            current salary data.
          </p>
        </div>
      </section>

      <section className="section finalSection">
        <h2>Why this fits the hackathon</h2>

        <div className="fitGrid">
          <div>
            <h3>4 Band agents</h3>
            <p>
              Assessment, mapping, planning, and review are handled by separate
              agents.
            </p>
          </div>

          <div>
            <h3>Meaningful Band usage</h3>
            <p>
              Agents pass structured context through visible Band handoffs, not
              just final notifications.
            </p>
          </div>

          <div>
            <h3>Real business value</h3>
            <p>
              CATR can support students, parents, schools, counselors, and
              education-sector guidance programs.
            </p>
          </div>
        </div>
      </section>
    </main>
  );
}

export default App;