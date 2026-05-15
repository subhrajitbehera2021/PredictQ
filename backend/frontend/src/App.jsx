import { useState, useEffect, useRef } from "react";

// ─── Design tokens ────────────────────────────────────────────────────────────
const C = {
  navy: "#0B1120",
  navyMid: "#111827",
  navyLight: "#1a2332",
  slate: "#1e2d3e",
  slateLight: "#253347",
  cyan: "#06d6a0",
  cyanDim: "#04a87d",
  cyanGlow: "rgba(6,214,160,0.15)",
  blue: "#3b82f6",
  blueDim: "#2563eb",
  amber: "#f59e0b",
  red: "#ef4444",
  purple: "#8b5cf6",
  textPrimary: "#f1f5f9",
  textSecondary: "#94a3b8",
  textMuted: "#475569",
  border: "rgba(255,255,255,0.07)",
  borderHover: "rgba(6,214,160,0.3)",
  cardBg: "rgba(255,255,255,0.04)",
  cardBgHover: "rgba(255,255,255,0.07)",
};

const font = `'DM Sans', 'Segoe UI', sans-serif`;
const mono = `'JetBrains Mono', 'Fira Code', monospace`;

const globalStyle = `
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=JetBrains+Mono:wght@400;500&display=swap');
  * { box-sizing: border-box; margin: 0; padding: 0; }
  :root { color-scheme: dark; }
  body { background: ${C.navy}; color: ${C.textPrimary}; font-family: ${font}; overflow-x: hidden; }
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: ${C.navyMid}; }
  ::-webkit-scrollbar-thumb { background: ${C.slateLight}; border-radius: 3px; }
  ::-webkit-scrollbar-thumb:hover { background: ${C.cyan}; }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }
  @keyframes slideIn { from{opacity:0;transform:translateY(12px)} to{opacity:1;transform:translateY(0)} }
  @keyframes fadeIn { from{opacity:0} to{opacity:1} }
  @keyframes ticker { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
  @keyframes ripple { 0%{transform:scale(1);opacity:0.6} 100%{transform:scale(2.5);opacity:0} }
  @keyframes spin { to{transform:rotate(360deg)} }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }
`;

// ─── Mock data ─────────────────────────────────────────────────────────────────
const MOCK = {
  hospitals: [
    { id: 1, name: "AIIMS New Delhi", city: "Delhi", status: "active", patients: 2840, plan: "Enterprise", score: 98 },
    { id: 2, name: "Apollo Hospitals", city: "Chennai", status: "active", patients: 1920, plan: "Pro", score: 94 },
    { id: 3, name: "Fortis Healthcare", city: "Mumbai", status: "active", patients: 1540, plan: "Pro", score: 91 },
    { id: 4, name: "Narayana Health", city: "Bengaluru", status: "trial", patients: 870, plan: "Starter", score: 87 },
    { id: 5, name: "Medanta Hospital", city: "Gurugram", status: "active", patients: 1230, plan: "Enterprise", score: 96 },
  ],
  doctors: [
    { id: 1, name: "Dr. Priya Sharma", dept: "Cardiology", status: "consulting", queue: 8, avg: "14 min", next: "2 min" },
    { id: 2, name: "Dr. Rohan Mehta", dept: "Neurology", status: "available", queue: 3, avg: "18 min", next: "now" },
    { id: 3, name: "Dr. Ananya Patel", dept: "Orthopedics", status: "break", queue: 5, avg: "12 min", next: "25 min" },
    { id: 4, name: "Dr. Vikram Singh", dept: "Dermatology", status: "consulting", queue: 12, avg: "10 min", next: "5 min" },
    { id: 5, name: "Dr. Kavitha Rao", dept: "Pediatrics", status: "available", queue: 1, avg: "20 min", next: "now" },
  ],
  queueLive: [
    { token: "A001", name: "Ramesh Kumar", dept: "Cardiology", wait: "~8 min", priority: "normal", status: "in-queue" },
    { token: "A002", name: "Sunita Devi", dept: "Cardiology", wait: "~22 min", priority: "normal", status: "in-queue" },
    { token: "B001", name: "Mahesh Gupta", dept: "Neurology", wait: "~5 min", priority: "normal", status: "in-queue" },
    { token: "E001", name: "Anjali Singh", dept: "Emergency", wait: "Immediate", priority: "emergency", status: "in-queue" },
    { token: "A000", name: "Pradeep Nair", dept: "Cardiology", wait: "—", priority: "normal", status: "consulting" },
  ],
  appointments: [
    { id: "APT001", patient: "Ravi Shankar", doctor: "Dr. Priya Sharma", dept: "Cardiology", time: "10:00 AM", status: "confirmed", type: "Follow-up" },
    { id: "APT002", patient: "Meena Kumari", doctor: "Dr. Rohan Mehta", dept: "Neurology", time: "10:30 AM", status: "checked-in", type: "New" },
    { id: "APT003", patient: "Ajay Verma", doctor: "Dr. Kavitha Rao", dept: "Pediatrics", time: "11:00 AM", status: "pending", type: "New" },
    { id: "APT004", patient: "Lalitha Devi", doctor: "Dr. Vikram Singh", dept: "Dermatology", time: "11:30 AM", status: "confirmed", type: "Follow-up" },
    { id: "APT005", patient: "Sanjay Gupta", doctor: "Dr. Ananya Patel", dept: "Orthopedics", time: "12:00 PM", status: "cancelled", type: "New" },
  ],
  notifications: [
    { id: 1, type: "emergency", title: "Emergency patient admitted", body: "Patient Anjali Singh requires immediate attention — Cardiology", time: "2 min ago", read: false },
    { id: 2, type: "ai", title: "AI Queue Forecast", body: "Neurology dept predicted to peak in 45 min. Consider rerouting.", time: "12 min ago", read: false },
    { id: 3, type: "system", title: "Queue threshold alert", body: "Cardiology queue > 10 patients. Dr. Sharma notified.", time: "28 min ago", read: true },
    { id: 4, type: "success", title: "Appointment completed", body: "APT-0098 consultation complete. Token A000 cleared.", time: "34 min ago", read: true },
    { id: 5, type: "ai", title: "Smart Recommendation", body: "Based on historical data, suggest adding 1 more slot on Tuesdays.", time: "1 hr ago", read: true },
  ],
};

// ─── Utility components ────────────────────────────────────────────────────────
const Badge = ({ color, children, pulse }) => {
  const colors = {
    green: { bg: "rgba(6,214,160,0.15)", text: C.cyan, border: "rgba(6,214,160,0.3)" },
    red: { bg: "rgba(239,68,68,0.15)", text: "#f87171", border: "rgba(239,68,68,0.3)" },
    amber: { bg: "rgba(245,158,11,0.15)", text: "#fbbf24", border: "rgba(245,158,11,0.3)" },
    blue: { bg: "rgba(59,130,246,0.15)", text: "#60a5fa", border: "rgba(59,130,246,0.3)" },
    purple: { bg: "rgba(139,92,246,0.15)", text: "#a78bfa", border: "rgba(139,92,246,0.3)" },
    gray: { bg: "rgba(255,255,255,0.08)", text: C.textSecondary, border: "rgba(255,255,255,0.12)" },
  };
  const s = colors[color] || colors.gray;
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: 5, background: s.bg, color: s.text, border: `1px solid ${s.border}`, borderRadius: 20, padding: "2px 10px", fontSize: 11, fontWeight: 500, fontFamily: font, whiteSpace: "nowrap" }}>
      {pulse && <span style={{ width: 6, height: 6, borderRadius: "50%", background: s.text, animation: "pulse 1.5s ease-in-out infinite", display: "inline-block" }} />}
      {children}
    </span>
  );
};

const StatCard = ({ label, value, sub, color, icon, trend }) => (
  <div style={{ background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 12, padding: "20px 22px", animation: "slideIn 0.4s ease", display: "flex", flexDirection: "column", gap: 8 }}>
    <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
      <span style={{ fontSize: 12, color: C.textMuted, fontWeight: 500, textTransform: "uppercase", letterSpacing: "0.08em" }}>{label}</span>
      {icon && <span style={{ fontSize: 18, opacity: 0.6 }}>{icon}</span>}
    </div>
    <div style={{ fontSize: 32, fontWeight: 700, color: color || C.textPrimary, fontFamily: mono, lineHeight: 1 }}>{value}</div>
    {sub && <div style={{ fontSize: 12, color: C.textSecondary }}>{sub}</div>}
    {trend && <div style={{ fontSize: 12, color: trend > 0 ? C.cyan : C.red }}>{trend > 0 ? "↑" : "↓"} {Math.abs(trend)}% vs yesterday</div>}
  </div>
);

const Card = ({ children, style }) => (
  <div style={{ background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 14, padding: 20, animation: "slideIn 0.4s ease", ...style }}>
    {children}
  </div>
);

const Btn = ({ children, onClick, variant = "primary", size = "md", style }) => {
  const variants = {
    primary: { background: C.cyan, color: C.navy, border: "none" },
    ghost: { background: "transparent", color: C.textPrimary, border: `1px solid ${C.border}` },
    danger: { background: "rgba(239,68,68,0.15)", color: "#f87171", border: "1px solid rgba(239,68,68,0.3)" },
    cyan: { background: C.cyanGlow, color: C.cyan, border: `1px solid rgba(6,214,160,0.3)` },
  };
  const sizes = { sm: { padding: "5px 12px", fontSize: 12 }, md: { padding: "8px 18px", fontSize: 13 }, lg: { padding: "11px 24px", fontSize: 14 } };
  return (
    <button onClick={onClick} style={{ ...variants[variant], ...sizes[size], borderRadius: 8, fontWeight: 600, cursor: "pointer", fontFamily: font, transition: "all 0.2s", ...style }}>
      {children}
    </button>
  );
};

const SectionHeader = ({ title, sub, action }) => (
  <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between", marginBottom: 20 }}>
    <div>
      <h2 style={{ fontSize: 20, fontWeight: 700, color: C.textPrimary, marginBottom: 4 }}>{title}</h2>
      {sub && <p style={{ fontSize: 13, color: C.textSecondary }}>{sub}</p>}
    </div>
    {action}
  </div>
);

const LiveDot = ({ color = C.cyan }) => (
  <span style={{ display: "inline-block", width: 8, height: 8, borderRadius: "50%", background: color, animation: "pulse 1.5s ease-in-out infinite", flexShrink: 0 }} />
);

const MiniChart = ({ data, color }) => {
  const max = Math.max(...data);
  const pts = data.map((v, i) => `${(i / (data.length - 1)) * 100},${100 - (v / max) * 100}`).join(" ");
  return (
    <svg viewBox="0 0 100 60" style={{ width: "100%", height: 50 }} preserveAspectRatio="none">
      <polyline points={pts} fill="none" stroke={color || C.cyan} strokeWidth="2" />
      <polygon points={`0,100 ${pts} 100,100`} fill={color || C.cyan} fillOpacity="0.1" />
    </svg>
  );
};

// ─── Navigation ────────────────────────────────────────────────────────────────
const NAV_ROLES = ["Super Admin", "Hospital Admin", "Doctor", "Staff", "Patient"];

const PAGES = {
  "Super Admin": [
    { key: "sa-dash", label: "Dashboard", icon: "⬡" },
    { key: "sa-hospitals", label: "Hospitals", icon: "🏥" },
    { key: "sa-users", label: "Users", icon: "👥" },
    { key: "sa-subscriptions", label: "Subscriptions", icon: "💳" },
    { key: "sa-ai", label: "AI Overview", icon: "🤖" },
    { key: "sa-settings", label: "Settings", icon: "⚙" },
  ],
  "Hospital Admin": [
    { key: "ha-dash", label: "Dashboard", icon: "⬡" },
    { key: "ha-queues", label: "Live Queue", icon: "⋯" },
    { key: "ha-doctors", label: "Doctors", icon: "👨‍⚕️" },
    { key: "ha-departments", label: "Departments", icon: "🏗" },
    { key: "ha-patients", label: "Patients", icon: "🫀" },
    { key: "ha-staff", label: "Staff", icon: "👷" },
    { key: "ha-reports", label: "Reports", icon: "📊" },
  ],
  Doctor: [
    { key: "dr-dash", label: "Dashboard", icon: "⬡" },
    { key: "dr-patients", label: "My Patients", icon: "🫀" },
    { key: "dr-appointments", label: "Appointments", icon: "📅" },
    { key: "dr-queue", label: "Queue Status", icon: "⋯" },
    { key: "dr-availability", label: "Availability", icon: "🕐" },
    { key: "dr-notes", label: "Notes", icon: "📝" },
  ],
  Staff: [
    { key: "st-dash", label: "Dashboard", icon: "⬡" },
    { key: "st-queue", label: "Queue Mgmt", icon: "⋯" },
    { key: "st-scanner", label: "Scanner", icon: "📲" },
    { key: "st-walkin", label: "Walk-in", icon: "🚶" },
    { key: "st-emergency", label: "Emergency", icon: "🚨" },
  ],
  Patient: [
    { key: "pt-dash", label: "Dashboard", icon: "⬡" },
    { key: "pt-book", label: "Book Appointment", icon: "📅" },
    { key: "pt-appointments", label: "My Appointments", icon: "📋" },
    { key: "pt-track", label: "Queue Tracking", icon: "📍" },
    { key: "pt-history", label: "Medical History", icon: "📂" },
    { key: "pt-payments", label: "Payments", icon: "💳" },
  ],
};

// ─── Page Components ───────────────────────────────────────────────────────────
const SuperAdminDash = () => {
  const [tick, setTick] = useState(0);
  useEffect(() => { const t = setInterval(() => setTick(x => x + 1), 3000); return () => clearInterval(t); }, []);
  const totalPatients = 9400 + tick * 2;

  return (
    <div style={{ animation: "slideIn 0.4s ease" }}>
      {/* Ticker */}
      <div style={{ background: C.navy, borderBottom: `1px solid ${C.border}`, padding: "8px 0", overflow: "hidden", marginBottom: 24 }}>
        <div style={{ display: "flex", gap: 32, whiteSpace: "nowrap", animation: "ticker 30s linear infinite" }}>
          {["🏥 5 Hospitals Active", "👨‍⚕️ 142 Doctors Online", "⋯ 2,840 Queue Today", "🤖 AI Accuracy: 94.7%", "📊 Revenue ₹48.2L Today", "🚨 2 Emergency Cases", "✅ 98.3% Uptime",
            "🏥 5 Hospitals Active", "👨‍⚕️ 142 Doctors Online", "⋯ 2,840 Queue Today", "🤖 AI Accuracy: 94.7%", "📊 Revenue ₹48.2L Today", "🚨 2 Emergency Cases", "✅ 98.3% Uptime"].map((t, i) => (
            <span key={i} style={{ fontSize: 12, color: C.textSecondary, fontFamily: mono }}>{t}</span>
          ))}
        </div>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16, marginBottom: 28 }}>
        <StatCard label="Total Hospitals" value="5" sub="All systems operational" color={C.cyan} icon="🏥" trend={0} />
        <StatCard label="Active Patients" value={totalPatients.toLocaleString()} sub="Across all hospitals" icon="👥" trend={8} />
        <StatCard label="AI Predictions" value="94.7%" sub="Model accuracy this week" color={C.purple} icon="🤖" trend={1.2} />
        <StatCard label="MRR" value="₹24.8L" sub="Monthly recurring revenue" color={C.amber} icon="💰" trend={12} />
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1.6fr 1fr", gap: 20, marginBottom: 24 }}>
        <Card>
          <SectionHeader title="Hospital Network" sub="Live status across all registered hospitals" />
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
            <thead>
              <tr style={{ borderBottom: `1px solid ${C.border}` }}>
                {["Hospital", "City", "Patients Today", "Plan", "Health"].map(h => (
                  <th key={h} style={{ padding: "8px 10px", textAlign: "left", color: C.textMuted, fontWeight: 500, fontSize: 11, textTransform: "uppercase" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {MOCK.hospitals.map(h => (
                <tr key={h.id} style={{ borderBottom: `1px solid ${C.border}` }}>
                  <td style={{ padding: "12px 10px", color: C.textPrimary, fontWeight: 500 }}>{h.name}</td>
                  <td style={{ padding: "12px 10px", color: C.textSecondary }}>{h.city}</td>
                  <td style={{ padding: "12px 10px", fontFamily: mono, color: C.cyan }}>{h.patients.toLocaleString()}</td>
                  <td style={{ padding: "12px 10px" }}><Badge color={h.plan === "Enterprise" ? "purple" : h.plan === "Pro" ? "blue" : "gray"}>{h.plan}</Badge></td>
                  <td style={{ padding: "12px 10px" }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                      <div style={{ flex: 1, height: 4, background: C.border, borderRadius: 2 }}>
                        <div style={{ width: `${h.score}%`, height: "100%", background: h.score > 93 ? C.cyan : C.amber, borderRadius: 2 }} />
                      </div>
                      <span style={{ fontSize: 11, fontFamily: mono, color: C.textSecondary }}>{h.score}%</span>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>

        <Card>
          <SectionHeader title="AI Pulse" sub="Real-time model telemetry" />
          <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
            {[
              { label: "Queue Prediction Accuracy", value: 94.7, color: C.cyan },
              { label: "Delay Forecast Precision", value: 88.2, color: C.blue },
              { label: "Emergency Detection Rate", value: 97.1, color: C.amber },
              { label: "Patient Flow Model", value: 91.4, color: C.purple },
            ].map(m => (
              <div key={m.label}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 5, fontSize: 12 }}>
                  <span style={{ color: C.textSecondary }}>{m.label}</span>
                  <span style={{ fontFamily: mono, color: m.color, fontWeight: 600 }}>{m.value}%</span>
                </div>
                <div style={{ height: 4, background: C.border, borderRadius: 2 }}>
                  <div style={{ width: `${m.value}%`, height: "100%", background: m.color, borderRadius: 2, transition: "width 0.6s ease" }} />
                </div>
              </div>
            ))}
          </div>
          <div style={{ marginTop: 20, padding: 12, background: C.cyanGlow, borderRadius: 8, border: `1px solid rgba(6,214,160,0.2)` }}>
            <div style={{ fontSize: 11, color: C.cyan, fontWeight: 600, marginBottom: 4 }}>🤖 AI INSIGHT</div>
            <div style={{ fontSize: 12, color: C.textSecondary }}>Cardiology dept shows 23% load spike in next 40 min. Auto-rebalancing queue suggested.</div>
          </div>
        </Card>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 20 }}>
        <Card>
          <SectionHeader title="Subscription Health" />
          <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
            {[{ name: "Enterprise", count: 2, color: C.purple }, { name: "Pro", count: 2, color: C.blue }, { name: "Starter / Trial", count: 1, color: C.textMuted }].map(p => (
              <div key={p.name} style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "10px 12px", background: C.cardBgHover, borderRadius: 8 }}>
                <span style={{ fontSize: 13, color: C.textSecondary }}>{p.name}</span>
                <span style={{ fontFamily: mono, fontWeight: 700, color: p.color, fontSize: 18 }}>{p.count}</span>
              </div>
            ))}
          </div>
        </Card>
        <Card>
          <SectionHeader title="System Health" />
          <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
            {[
              { name: "API Uptime", val: "99.98%", ok: true },
              { name: "WebSocket", val: "Active", ok: true },
              { name: "AI Model", val: "Running", ok: true },
              { name: "DB Latency", val: "12ms", ok: true },
            ].map(s => (
              <div key={s.name} style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <LiveDot color={s.ok ? C.cyan : C.red} />
                  <span style={{ fontSize: 13, color: C.textSecondary }}>{s.name}</span>
                </div>
                <span style={{ fontFamily: mono, fontSize: 12, color: s.ok ? C.cyan : C.red }}>{s.val}</span>
              </div>
            ))}
          </div>
        </Card>
        <Card>
          <SectionHeader title="Recent Activity" />
          <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
            {["New hospital AIIMS Bhubaneswar pending approval", "AI model retrained with 12K new records", "Apollo Hospitals upgraded to Enterprise", "Security patch v2.1.4 deployed"].map((a, i) => (
              <div key={i} style={{ fontSize: 12, color: C.textSecondary, padding: "8px 0", borderBottom: i < 3 ? `1px solid ${C.border}` : "none" }}>
                {a}
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
};

const HospitalAdminDash = () => {
  const [tick, setTick] = useState(0);
  useEffect(() => { const t = setInterval(() => setTick(x => x + 1), 2000); return () => clearInterval(t); }, []);

  return (
    <div style={{ animation: "slideIn 0.4s ease" }}>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16, marginBottom: 28 }}>
        <StatCard label="Queue Length" value={`${34 + tick % 4}`} sub="Across all departments" color={C.amber} icon="⋯" trend={-5} />
        <StatCard label="Avg Wait Time" value="18 min" sub="Down from 24 min yesterday" color={C.cyan} icon="⏱" trend={-12} />
        <StatCard label="Doctors Active" value="9 / 14" sub="5 on break/offline" icon="👨‍⚕️" />
        <StatCard label="Today's Patients" value="284" sub="67 remaining in queues" color={C.purple} icon="🫀" trend={6} />
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1.4fr 1fr", gap: 20, marginBottom: 24 }}>
        <Card>
          <SectionHeader title="Live Queue Monitor" sub="Real-time across all departments" action={<Badge color="green" pulse>LIVE</Badge>} />
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {MOCK.queueLive.map((q, i) => (
              <div key={i} style={{ display: "flex", alignItems: "center", gap: 12, padding: "10px 14px", background: q.priority === "emergency" ? "rgba(239,68,68,0.08)" : C.cardBgHover, borderRadius: 10, border: `1px solid ${q.priority === "emergency" ? "rgba(239,68,68,0.25)" : C.border}` }}>
                <span style={{ fontFamily: mono, fontSize: 13, color: q.priority === "emergency" ? "#f87171" : C.cyan, fontWeight: 700, minWidth: 44 }}>{q.token}</span>
                <div style={{ flex: 1 }}>
                  <div style={{ fontSize: 13, fontWeight: 500, color: C.textPrimary }}>{q.name}</div>
                  <div style={{ fontSize: 11, color: C.textSecondary }}>{q.dept}</div>
                </div>
                <Badge color={q.priority === "emergency" ? "red" : q.status === "consulting" ? "green" : "amber"}>
                  {q.priority === "emergency" ? "EMERGENCY" : q.status === "consulting" ? "Consulting" : q.wait}
                </Badge>
              </div>
            ))}
          </div>
        </Card>

        <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
          <Card>
            <SectionHeader title="Department Load" />
            <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              {[
                { dept: "Cardiology", load: 82, queue: 8 },
                { dept: "Neurology", load: 45, queue: 3 },
                { dept: "Orthopedics", load: 67, queue: 5 },
                { dept: "Dermatology", load: 90, queue: 12 },
                { dept: "Pediatrics", load: 28, queue: 1 },
              ].map(d => (
                <div key={d.dept}>
                  <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4, fontSize: 12 }}>
                    <span style={{ color: C.textSecondary }}>{d.dept}</span>
                    <span style={{ fontFamily: mono, color: d.load > 80 ? C.red : d.load > 60 ? C.amber : C.cyan }}>{d.queue} waiting</span>
                  </div>
                  <div style={{ height: 6, background: C.border, borderRadius: 3 }}>
                    <div style={{ width: `${d.load}%`, height: "100%", background: d.load > 80 ? C.red : d.load > 60 ? C.amber : C.cyan, borderRadius: 3, transition: "width 0.6s" }} />
                  </div>
                </div>
              ))}
            </div>
          </Card>
          <Card style={{ background: "rgba(139,92,246,0.08)", border: "1px solid rgba(139,92,246,0.25)" }}>
            <div style={{ fontSize: 11, color: C.purple, fontWeight: 700, marginBottom: 8 }}>🤖 AI RECOMMENDATION</div>
            <p style={{ fontSize: 13, color: C.textSecondary, lineHeight: 1.6 }}>Dermatology is nearing critical load. Suggest reassigning 3 non-urgent cases to afternoon slots. Estimated wait reduction: <strong style={{ color: C.cyan }}>14 minutes</strong>.</p>
            <div style={{ marginTop: 12, display: "flex", gap: 8 }}>
              <Btn variant="cyan" size="sm">Apply</Btn>
              <Btn variant="ghost" size="sm">Dismiss</Btn>
            </div>
          </Card>
        </div>
      </div>

      <Card>
        <SectionHeader title="Doctor Status Overview" />
        <div style={{ display: "grid", gridTemplateColumns: "repeat(5,1fr)", gap: 12 }}>
          {MOCK.doctors.map(d => (
            <div key={d.id} style={{ padding: "14px", background: C.cardBgHover, borderRadius: 10, border: `1px solid ${C.border}`, textAlign: "center" }}>
              <div style={{ width: 44, height: 44, borderRadius: "50%", background: d.status === "available" ? "rgba(6,214,160,0.15)" : d.status === "consulting" ? "rgba(59,130,246,0.15)" : C.border, display: "flex", alignItems: "center", justifyContent: "center", margin: "0 auto 10px", fontSize: 20 }}>👨‍⚕️</div>
              <div style={{ fontSize: 12, fontWeight: 600, color: C.textPrimary, marginBottom: 4 }}>{d.name.replace("Dr. ", "")}</div>
              <div style={{ fontSize: 11, color: C.textMuted, marginBottom: 8 }}>{d.dept}</div>
              <Badge color={d.status === "available" ? "green" : d.status === "consulting" ? "blue" : "gray"}>
                {d.status === "available" ? "Available" : d.status === "consulting" ? "Consulting" : "Break"}
              </Badge>
              <div style={{ marginTop: 8, fontSize: 11, fontFamily: mono, color: C.textMuted }}>{d.queue} in queue</div>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};

const DoctorDash = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <div style={{ marginBottom: 20, padding: "16px 20px", background: "rgba(6,214,160,0.07)", border: `1px solid rgba(6,214,160,0.2)`, borderRadius: 12, display: "flex", alignItems: "center", gap: 14 }}>
      <div style={{ width: 52, height: 52, borderRadius: "50%", background: C.cyanGlow, border: `2px solid ${C.cyan}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 24 }}>👨‍⚕️</div>
      <div>
        <div style={{ fontSize: 16, fontWeight: 700, color: C.textPrimary }}>Good morning, Dr. Priya Sharma</div>
        <div style={{ fontSize: 13, color: C.textSecondary }}>Cardiology • AIIMS New Delhi • <span style={{ color: C.cyan }}>Currently Consulting</span></div>
      </div>
      <div style={{ marginLeft: "auto", display: "flex", gap: 10 }}>
        <Btn variant="cyan" size="sm">Start Break</Btn>
        <Btn variant="ghost" size="sm">Mark Unavailable</Btn>
      </div>
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16, marginBottom: 24 }}>
      <StatCard label="Today's Patients" value="12" sub="4 remaining" color={C.cyan} icon="🫀" />
      <StatCard label="Avg Consult Time" value="14 min" sub="Target: 15 min" color={C.green} icon="⏱" />
      <StatCard label="Queue Now" value="8" sub="Est. 2h 20m total" color={C.amber} icon="⋯" />
      <StatCard label="Next Patient" value="2 min" sub="Token A001 — Ramesh Kumar" color={C.purple} icon="⏭" />
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "1.5fr 1fr", gap: 20 }}>
      <Card>
        <SectionHeader title="Today's Queue" sub="Cardiology — Dr. Priya Sharma" action={<Badge color="blue" pulse>8 waiting</Badge>} />
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          {[
            { token: "A000", name: "Pradeep Nair", age: 54, type: "Follow-up", status: "consulting" },
            { token: "A001", name: "Ramesh Kumar", age: 42, type: "New", status: "next" },
            { token: "A002", name: "Sunita Devi", age: 38, type: "Follow-up", status: "waiting" },
            { token: "A003", name: "Mohan Lal", age: 67, type: "New", status: "waiting" },
            { token: "A004", name: "Geeta Sharma", age: 45, type: "New", status: "waiting" },
          ].map((p, i) => (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 12, padding: "10px 12px", background: p.status === "consulting" ? "rgba(6,214,160,0.08)" : p.status === "next" ? "rgba(59,130,246,0.08)" : "transparent", borderRadius: 8, border: `1px solid ${p.status === "consulting" ? "rgba(6,214,160,0.2)" : p.status === "next" ? "rgba(59,130,246,0.2)" : "transparent"}` }}>
              <span style={{ fontFamily: mono, fontSize: 12, color: p.status === "consulting" ? C.cyan : p.status === "next" ? C.blue : C.textMuted, minWidth: 36 }}>{p.token}</span>
              <div style={{ flex: 1 }}>
                <span style={{ fontSize: 13, fontWeight: 500, color: C.textPrimary }}>{p.name}</span>
                <span style={{ fontSize: 11, color: C.textMuted, marginLeft: 8 }}>{p.age}y</span>
              </div>
              <Badge color="gray">{p.type}</Badge>
              <Badge color={p.status === "consulting" ? "green" : p.status === "next" ? "blue" : "gray"}>
                {p.status === "consulting" ? "Now" : p.status === "next" ? "Next" : "Waiting"}
              </Badge>
            </div>
          ))}
        </div>
        <div style={{ marginTop: 16, display: "flex", gap: 10 }}>
          <Btn variant="primary" size="md">Call Next Patient</Btn>
          <Btn variant="ghost" size="md">Skip Token</Btn>
        </div>
      </Card>

      <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
        <Card>
          <SectionHeader title="Current Patient" />
          <div style={{ padding: "14px", background: C.cardBgHover, borderRadius: 10, marginBottom: 12 }}>
            <div style={{ fontSize: 14, fontWeight: 600, color: C.textPrimary, marginBottom: 4 }}>Pradeep Nair — 54y, Male</div>
            <div style={{ fontSize: 12, color: C.textSecondary, marginBottom: 10 }}>Token: A000 • Follow-up • Cardiology</div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8, fontSize: 12 }}>
              <div style={{ color: C.textMuted }}>BP: <span style={{ color: C.textPrimary }}>140/90</span></div>
              <div style={{ color: C.textMuted }}>HR: <span style={{ color: C.textPrimary }}>78 bpm</span></div>
              <div style={{ color: C.textMuted }}>Temp: <span style={{ color: C.textPrimary }}>98.4°F</span></div>
              <div style={{ color: C.textMuted }}>SPO2: <span style={{ color: C.cyan }}>98%</span></div>
            </div>
          </div>
          <div style={{ display: "flex", gap: 8 }}>
            <Btn variant="cyan" size="sm">Add Note</Btn>
            <Btn variant="ghost" size="sm">Prescribe</Btn>
            <Btn variant="primary" size="sm">Complete</Btn>
          </div>
        </Card>
        <Card>
          <SectionHeader title="Schedule Today" />
          <div style={{ display: "flex", flexDirection: "column", gap: 6, fontSize: 12 }}>
            {["9:00 AM — OPD Start", "10:30 AM — Case Review (virtual)", "1:00 PM — Lunch Break", "2:00 PM — Afternoon OPD", "5:00 PM — End of Duty"].map((s, i) => (
              <div key={i} style={{ display: "flex", alignItems: "center", gap: 8, padding: "6px 0", borderBottom: i < 4 ? `1px solid ${C.border}` : "none" }}>
                <LiveDot color={i < 2 ? C.textMuted : C.cyan} />
                <span style={{ color: i < 2 ? C.textMuted : C.textSecondary }}>{s}</span>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  </div>
);

const PatientDash = () => {
  const [tokenStep, setTokenStep] = useState(3);
  useEffect(() => { const t = setInterval(() => setTokenStep(s => Math.max(1, s - (Math.random() > 0.7 ? 1 : 0))), 4000); return () => clearInterval(t); }, []);

  return (
    <div style={{ animation: "slideIn 0.4s ease" }}>
      <div style={{ marginBottom: 20, padding: "16px 20px", background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 12, display: "flex", alignItems: "center", gap: 14 }}>
        <div style={{ width: 52, height: 52, borderRadius: "50%", background: "rgba(59,130,246,0.15)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 24 }}>🫀</div>
        <div>
          <div style={{ fontSize: 16, fontWeight: 700, color: C.textPrimary }}>Welcome back, Ravi Shankar</div>
          <div style={{ fontSize: 13, color: C.textSecondary }}>Patient ID: PAT-0098 • AIIMS New Delhi</div>
        </div>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 20, marginBottom: 24 }}>
        {/* Token tracker */}
        <Card style={{ gridColumn: "1", background: "rgba(6,214,160,0.05)", border: "1px solid rgba(6,214,160,0.2)" }}>
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 11, color: C.cyan, fontWeight: 700, marginBottom: 12, letterSpacing: "0.1em" }}>YOUR TOKEN</div>
            <div style={{ fontSize: 56, fontWeight: 800, fontFamily: mono, color: C.cyan, lineHeight: 1 }}>A00{tokenStep + 1}</div>
            <div style={{ fontSize: 13, color: C.textSecondary, margin: "12px 0 4px" }}>Position in queue</div>
            <div style={{ fontSize: 32, fontWeight: 700, color: C.textPrimary, fontFamily: mono }}>#{tokenStep}</div>
            <div style={{ marginTop: 12, padding: "8px 14px", background: C.cyanGlow, borderRadius: 8, fontSize: 12, color: C.cyan }}>
              ⏱ Est. wait: ~{tokenStep * 14} minutes
            </div>
            <div style={{ marginTop: 10, fontSize: 11, color: C.textMuted }}>AI confidence: 91% accurate</div>
          </div>
        </Card>

        <Card>
          <SectionHeader title="Upcoming Appointments" />
          <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
            {[
              { date: "Today", time: "10:00 AM", doctor: "Dr. Priya Sharma", dept: "Cardiology", status: "confirmed" },
              { date: "May 18", time: "11:30 AM", doctor: "Dr. Rohan Mehta", dept: "Neurology", status: "pending" },
            ].map((a, i) => (
              <div key={i} style={{ padding: "12px", background: C.cardBgHover, borderRadius: 10 }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                  <Badge color={a.status === "confirmed" ? "green" : "amber"}>{a.status}</Badge>
                  <span style={{ fontSize: 11, fontFamily: mono, color: C.textMuted }}>{a.date}</span>
                </div>
                <div style={{ fontSize: 13, fontWeight: 600, color: C.textPrimary }}>{a.doctor}</div>
                <div style={{ fontSize: 11, color: C.textSecondary }}>{a.dept} • {a.time}</div>
              </div>
            ))}
            <Btn variant="cyan" size="sm" style={{ marginTop: 4 }}>+ Book New Appointment</Btn>
          </div>
        </Card>

        <Card>
          <SectionHeader title="Doctor Status" />
          <div style={{ marginBottom: 16, padding: "14px", background: C.cardBgHover, borderRadius: 10 }}>
            <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
              <LiveDot />
              <span style={{ fontWeight: 600, color: C.textPrimary, fontSize: 14 }}>Dr. Priya Sharma</span>
            </div>
            <div style={{ fontSize: 12, color: C.textSecondary, marginBottom: 6 }}>Cardiology • Currently Consulting</div>
            <div style={{ fontSize: 11, color: C.textMuted }}>Avg consult: 14 min • 8 in queue ahead</div>
          </div>
          <div style={{ fontSize: 12, color: C.textSecondary, marginBottom: 8 }}>AI Forecast:</div>
          <div style={{ height: 40 }}>
            <MiniChart data={[5, 8, 12, 10, 14, 9, 7, 5, 8, 6, 4, 3]} color={C.cyan} />
          </div>
          <div style={{ fontSize: 11, color: C.textMuted, marginTop: 4 }}>Queue load — last 12 hours</div>
        </Card>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "1.5fr 1fr", gap: 20 }}>
        <Card>
          <SectionHeader title="Appointment History" />
          <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
            <thead>
              <tr style={{ borderBottom: `1px solid ${C.border}` }}>
                {["Date", "Doctor", "Dept", "Status"].map(h => (
                  <th key={h} style={{ padding: "6px 8px", textAlign: "left", color: C.textMuted, fontWeight: 500, fontSize: 11, textTransform: "uppercase" }}>{h}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {[
                { date: "May 5", doctor: "Dr. Sharma", dept: "Cardiology", status: "completed" },
                { date: "Apr 22", doctor: "Dr. Mehta", dept: "Neurology", status: "completed" },
                { date: "Apr 10", doctor: "Dr. Patel", dept: "Orthopedics", status: "cancelled" },
                { date: "Mar 28", doctor: "Dr. Sharma", dept: "Cardiology", status: "completed" },
              ].map((r, i) => (
                <tr key={i} style={{ borderBottom: `1px solid ${C.border}` }}>
                  <td style={{ padding: "10px 8px", fontFamily: mono, color: C.textMuted, fontSize: 12 }}>{r.date}</td>
                  <td style={{ padding: "10px 8px", color: C.textSecondary }}>{r.doctor}</td>
                  <td style={{ padding: "10px 8px", color: C.textMuted, fontSize: 12 }}>{r.dept}</td>
                  <td style={{ padding: "10px 8px" }}><Badge color={r.status === "completed" ? "green" : "red"}>{r.status}</Badge></td>
                </tr>
              ))}
            </tbody>
          </table>
        </Card>

        <Card>
          <SectionHeader title="Notifications" />
          <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
            {MOCK.notifications.slice(0, 3).map(n => (
              <div key={n.id} style={{ padding: "10px 12px", background: n.read ? "transparent" : C.cardBgHover, borderRadius: 8, border: `1px solid ${n.read ? "transparent" : C.border}` }}>
                <div style={{ fontSize: 12, fontWeight: 600, color: n.type === "emergency" ? "#f87171" : n.type === "ai" ? C.purple : C.textPrimary, marginBottom: 3 }}>{n.title}</div>
                <div style={{ fontSize: 11, color: C.textSecondary, marginBottom: 4 }}>{n.body}</div>
                <div style={{ fontSize: 10, color: C.textMuted }}>{n.time}</div>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  );
};

const StaffDash = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16, marginBottom: 24 }}>
      <StatCard label="Total in Queue" value="34" sub="All departments" color={C.cyan} icon="⋯" />
      <StatCard label="Check-ins Today" value="156" sub="12 in last hour" icon="✅" trend={8} />
      <StatCard label="Walk-ins" value="23" sub="Registered today" color={C.amber} icon="🚶" />
      <StatCard label="Emergency" value="2" sub="Active cases" color={C.red} icon="🚨" />
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "1.5fr 1fr", gap: 20, marginBottom: 20 }}>
      <Card>
        <SectionHeader title="Queue Management Panel" sub="Manage live patient flow" action={<Badge color="green" pulse>LIVE</Badge>} />
        <div style={{ display: "flex", gap: 10, marginBottom: 16 }}>
          <Btn variant="primary">+ Add Walk-in</Btn>
          <Btn variant="cyan">Scan QR / Token</Btn>
          <Btn variant="ghost">Emergency Admit</Btn>
        </div>
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          {MOCK.queueLive.map((q, i) => (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 10, padding: "10px 12px", background: q.priority === "emergency" ? "rgba(239,68,68,0.08)" : C.cardBgHover, borderRadius: 8, border: `1px solid ${q.priority === "emergency" ? "rgba(239,68,68,0.2)" : C.border}` }}>
              <span style={{ fontFamily: mono, color: q.priority === "emergency" ? "#f87171" : C.cyan, fontWeight: 700, fontSize: 13 }}>{q.token}</span>
              <div style={{ flex: 1 }}>
                <div style={{ fontSize: 13, color: C.textPrimary }}>{q.name}</div>
                <div style={{ fontSize: 11, color: C.textMuted }}>{q.dept}</div>
              </div>
              <Badge color={q.priority === "emergency" ? "red" : q.status === "consulting" ? "green" : "amber"}>
                {q.priority === "emergency" ? "🚨 Emergency" : q.wait}
              </Badge>
              <div style={{ display: "flex", gap: 6 }}>
                <button style={{ fontSize: 11, padding: "4px 8px", background: C.cyanGlow, border: `1px solid rgba(6,214,160,0.2)`, borderRadius: 6, color: C.cyan, cursor: "pointer" }}>✓</button>
                <button style={{ fontSize: 11, padding: "4px 8px", background: "rgba(239,68,68,0.1)", border: "1px solid rgba(239,68,68,0.2)", borderRadius: 6, color: "#f87171", cursor: "pointer" }}>×</button>
              </div>
            </div>
          ))}
        </div>
      </Card>

      <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
        <Card style={{ background: "rgba(239,68,68,0.05)", border: "1px solid rgba(239,68,68,0.2)" }}>
          <SectionHeader title="🚨 Emergency Cases" />
          <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
            {[
              { name: "Anjali Singh", age: 34, condition: "Chest Pain", time: "2 min ago" },
              { name: "Ramesh Yadav", age: 68, condition: "Stroke Symptoms", time: "14 min ago" },
            ].map((e, i) => (
              <div key={i} style={{ padding: "10px 12px", background: "rgba(239,68,68,0.08)", borderRadius: 8, border: "1px solid rgba(239,68,68,0.2)" }}>
                <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 4 }}>
                  <span style={{ fontSize: 13, fontWeight: 600, color: "#f87171" }}>{e.name}, {e.age}y</span>
                  <span style={{ fontSize: 11, color: C.textMuted }}>{e.time}</span>
                </div>
                <div style={{ fontSize: 12, color: C.textSecondary }}>{e.condition}</div>
                <div style={{ marginTop: 8, display: "flex", gap: 6 }}>
                  <Btn variant="danger" size="sm">Escalate</Btn>
                  <Btn variant="ghost" size="sm">Assign Doctor</Btn>
                </div>
              </div>
            ))}
          </div>
        </Card>

        <Card>
          <SectionHeader title="Today's Appointments" />
          <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
            {MOCK.appointments.slice(0, 4).map(a => (
              <div key={a.id} style={{ display: "flex", alignItems: "center", justifyContent: "space-between", padding: "8px 10px", borderRadius: 8, background: C.cardBgHover }}>
                <div>
                  <div style={{ fontSize: 12, fontWeight: 500, color: C.textPrimary }}>{a.patient}</div>
                  <div style={{ fontSize: 11, color: C.textMuted }}>{a.time} • {a.dept}</div>
                </div>
                <Badge color={a.status === "confirmed" ? "green" : a.status === "checked-in" ? "blue" : a.status === "cancelled" ? "red" : "amber"}>{a.status}</Badge>
              </div>
            ))}
          </div>
        </Card>
      </div>
    </div>
  </div>
);

const AIPage = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <div style={{ marginBottom: 20, padding: "14px 18px", background: "rgba(139,92,246,0.08)", border: "1px solid rgba(139,92,246,0.25)", borderRadius: 12, display: "flex", alignItems: "center", gap: 12 }}>
      <span style={{ fontSize: 28 }}>🤖</span>
      <div>
        <div style={{ fontSize: 15, fontWeight: 700, color: C.textPrimary }}>QueueSense AI Engine — Active</div>
        <div style={{ fontSize: 12, color: C.textSecondary }}>Real-time queue prediction, delay forecasting, emergency prioritization & traffic analysis</div>
      </div>
      <Badge color="purple" pulse style={{ marginLeft: "auto" }}>MODEL v2.4</Badge>
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16, marginBottom: 24 }}>
      <StatCard label="Prediction Accuracy" value="94.7%" color={C.purple} icon="🎯" />
      <StatCard label="Avg Forecast Error" value="2.3 min" color={C.blue} icon="📊" />
      <StatCard label="Emergency Detections" value="98.1%" color={C.red} icon="🚨" />
      <StatCard label="Predictions Today" value="4,820" color={C.cyan} icon="⚡" />
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20, marginBottom: 20 }}>
      <Card>
        <SectionHeader title="Queue Prediction Model" sub="Next 2 hours forecast by department" />
        <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
          {[
            { dept: "Cardiology", now: 8, peak: 18, peakTime: "11:30 AM", risk: "high" },
            { dept: "Neurology", now: 3, peak: 7, peakTime: "12:00 PM", risk: "medium" },
            { dept: "Dermatology", now: 12, peak: 15, peakTime: "Now", risk: "high" },
            { dept: "Pediatrics", now: 1, peak: 4, peakTime: "2:00 PM", risk: "low" },
          ].map(d => (
            <div key={d.dept} style={{ padding: "12px 14px", background: C.cardBgHover, borderRadius: 10, border: `1px solid ${d.risk === "high" ? "rgba(239,68,68,0.2)" : d.risk === "medium" ? "rgba(245,158,11,0.2)" : "rgba(6,214,160,0.2)"}` }}>
              <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
                <span style={{ fontWeight: 600, fontSize: 13, color: C.textPrimary }}>{d.dept}</span>
                <Badge color={d.risk === "high" ? "red" : d.risk === "medium" ? "amber" : "green"}>{d.risk} load</Badge>
              </div>
              <div style={{ display: "flex", gap: 16, fontSize: 12, color: C.textSecondary }}>
                <span>Now: <strong style={{ color: C.textPrimary, fontFamily: mono }}>{d.now}</strong></span>
                <span>Peak: <strong style={{ color: d.risk === "high" ? "#f87171" : C.amber, fontFamily: mono }}>{d.peak}</strong></span>
                <span>At: <strong style={{ color: C.textPrimary }}>{d.peakTime}</strong></span>
              </div>
            </div>
          ))}
        </div>
      </Card>

      <Card>
        <SectionHeader title="AI Smart Recommendations" />
        <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
          {[
            { icon: "⚡", title: "Rebalance Queue", body: "Move 3 non-urgent Cardiology cases to afternoon slots. Est. improvement: -14 min avg wait.", action: "Apply", type: "primary" },
            { icon: "📅", title: "Schedule Optimization", body: "Add 2 extra slots on Tuesday mornings to handle recurring 30% peak.", action: "Schedule", type: "cyan" },
            { icon: "👨‍⚕️", title: "Doctor Allocation", body: "Dr. Rao (Pediatrics) has capacity. Consider cross-assigning 2 walk-in patients.", action: "Assign", type: "ghost" },
          ].map((r, i) => (
            <div key={i} style={{ padding: "12px 14px", background: "rgba(139,92,246,0.07)", borderRadius: 10, border: "1px solid rgba(139,92,246,0.18)" }}>
              <div style={{ display: "flex", alignItems: "flex-start", gap: 10 }}>
                <span style={{ fontSize: 18 }}>{r.icon}</span>
                <div style={{ flex: 1 }}>
                  <div style={{ fontSize: 13, fontWeight: 600, color: C.textPrimary, marginBottom: 4 }}>{r.title}</div>
                  <div style={{ fontSize: 12, color: C.textSecondary, lineHeight: 1.5, marginBottom: 8 }}>{r.body}</div>
                  <Btn variant={r.type} size="sm">{r.action}</Btn>
                </div>
              </div>
            </div>
          ))}
        </div>
      </Card>
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 20 }}>
      <Card>
        <SectionHeader title="Patient Flow Heatmap" sub="Hourly visits pattern" />
        <div style={{ display: "grid", gridTemplateColumns: "repeat(12,1fr)", gap: 3 }}>
          {Array.from({ length: 7 }, (_, day) =>
            Array.from({ length: 12 }, (_, hour) => {
              const intensity = Math.random();
              const bg = intensity > 0.7 ? C.red : intensity > 0.5 ? C.amber : intensity > 0.3 ? C.cyan : C.border;
              return <div key={`${day}-${hour}`} style={{ height: 16, borderRadius: 2, background: bg, opacity: 0.7 + intensity * 0.3 }} />;
            })
          )}
        </div>
        <div style={{ display: "flex", gap: 8, marginTop: 10, fontSize: 10, color: C.textMuted, alignItems: "center" }}>
          <div style={{ width: 10, height: 10, background: C.border, borderRadius: 2 }} /> Low
          <div style={{ width: 10, height: 10, background: C.cyan, borderRadius: 2 }} /> Medium
          <div style={{ width: 10, height: 10, background: C.amber, borderRadius: 2 }} /> High
          <div style={{ width: 10, height: 10, background: C.red, borderRadius: 2 }} /> Critical
        </div>
      </Card>

      <Card>
        <SectionHeader title="Emergency Priority AI" />
        <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
          {[
            { label: "Chest Pain / Heart Attack", score: 98, color: C.red },
            { label: "Stroke Symptoms", score: 97, color: C.red },
            { label: "Severe Trauma", score: 95, color: C.red },
            { label: "High Fever in Child", score: 84, color: C.amber },
            { label: "Fracture / Dislocation", score: 72, color: C.amber },
            { label: "General Illness", score: 40, color: C.cyan },
          ].map(e => (
            <div key={e.label} style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <div style={{ flex: 1, fontSize: 12, color: C.textSecondary }}>{e.label}</div>
              <div style={{ fontFamily: mono, fontSize: 12, color: e.color, minWidth: 32, textAlign: "right" }}>{e.score}</div>
            </div>
          ))}
          <div style={{ fontSize: 11, color: C.textMuted, marginTop: 4 }}>Priority scores (0–100) assigned by AI triage model</div>
        </div>
      </Card>

      <Card>
        <SectionHeader title="Model Accuracy Trend" />
        <MiniChart data={[88, 90, 89, 91, 93, 92, 94, 93, 95, 94, 95, 94.7]} color={C.purple} />
        <div style={{ fontSize: 11, color: C.textMuted, marginBottom: 12 }}>Last 12 weeks — Queue prediction accuracy %</div>
        <div style={{ display: "flex", flexDirection: "column", gap: 6, fontSize: 12 }}>
          {[
            { label: "Training samples", val: "4.2M" },
            { label: "Last retrained", val: "2 days ago" },
            { label: "Model version", val: "v2.4.1" },
            { label: "Inference time", val: "~38ms" },
          ].map(m => (
            <div key={m.label} style={{ display: "flex", justifyContent: "space-between" }}>
              <span style={{ color: C.textMuted }}>{m.label}</span>
              <span style={{ fontFamily: mono, color: C.textSecondary }}>{m.val}</span>
            </div>
          ))}
        </div>
      </Card>
    </div>
  </div>
);

const ReportsPage = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16, marginBottom: 24 }}>
      <StatCard label="Patients Today" value="284" trend={6} icon="🫀" />
      <StatCard label="Avg Wait Time" value="18 min" trend={-12} color={C.cyan} icon="⏱" />
      <StatCard label="Queue Resolved" value="261" trend={4} color={C.purple} icon="✅" />
      <StatCard label="Emergency Cases" value="7" trend={-3} color={C.red} icon="🚨" />
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20, marginBottom: 20 }}>
      <Card>
        <SectionHeader title="Department Performance" />
        <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 12 }}>
          <thead>
            <tr style={{ borderBottom: `1px solid ${C.border}` }}>
              {["Department", "Patients", "Avg Wait", "Resolved", "Rating"].map(h => (
                <th key={h} style={{ padding: "6px 8px", textAlign: "left", color: C.textMuted, fontWeight: 500, fontSize: 10, textTransform: "uppercase" }}>{h}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {[
              { dept: "Cardiology", patients: 68, wait: "14 min", resolved: 62, rating: 4.6 },
              { dept: "Neurology", patients: 42, wait: "18 min", resolved: 40, rating: 4.8 },
              { dept: "Orthopedics", patients: 55, wait: "12 min", resolved: 50, rating: 4.4 },
              { dept: "Dermatology", patients: 78, wait: "10 min", resolved: 74, rating: 4.5 },
              { dept: "Pediatrics", patients: 41, wait: "20 min", resolved: 35, rating: 4.9 },
            ].map((d, i) => (
              <tr key={i} style={{ borderBottom: `1px solid ${C.border}` }}>
                <td style={{ padding: "10px 8px", color: C.textPrimary, fontWeight: 500 }}>{d.dept}</td>
                <td style={{ padding: "10px 8px", fontFamily: mono, color: C.textSecondary }}>{d.patients}</td>
                <td style={{ padding: "10px 8px", color: C.textSecondary }}>{d.wait}</td>
                <td style={{ padding: "10px 8px", fontFamily: mono, color: C.cyan }}>{d.resolved}</td>
                <td style={{ padding: "10px 8px" }}><Badge color="green">⭐ {d.rating}</Badge></td>
              </tr>
            ))}
          </tbody>
        </table>
      </Card>

      <Card>
        <SectionHeader title="Patient Wait Distribution" />
        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
          {[
            { range: "0–10 min", count: 82, pct: 29 },
            { range: "10–20 min", count: 104, pct: 37 },
            { range: "20–30 min", count: 58, pct: 20 },
            { range: "30–45 min", count: 30, pct: 11 },
            { range: "45+ min", count: 10, pct: 3 },
          ].map(b => (
            <div key={b.range} style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span style={{ fontSize: 11, color: C.textMuted, minWidth: 72 }}>{b.range}</span>
              <div style={{ flex: 1, height: 20, background: C.border, borderRadius: 3, overflow: "hidden" }}>
                <div style={{ width: `${b.pct}%`, height: "100%", background: b.pct > 30 ? C.cyan : b.pct > 20 ? C.blue : C.slateLight, borderRadius: 3, display: "flex", alignItems: "center", paddingLeft: 6 }}>
                  <span style={{ fontSize: 10, color: b.pct > 10 ? C.navy : C.textSecondary, fontWeight: 600, fontFamily: mono }}>{b.pct}%</span>
                </div>
              </div>
              <span style={{ fontSize: 11, fontFamily: mono, color: C.textSecondary, minWidth: 32 }}>{b.count}</span>
            </div>
          ))}
        </div>
        <div style={{ marginTop: 16, display: "flex", gap: 8 }}>
          <Btn variant="cyan" size="sm">Export CSV</Btn>
          <Btn variant="ghost" size="sm">Export PDF</Btn>
        </div>
      </Card>
    </div>

    <Card>
      <SectionHeader title="Appointment Log" sub="Today's complete record" action={<Btn variant="ghost" size="sm">Export All</Btn>} />
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
        <thead>
          <tr style={{ borderBottom: `1px solid ${C.border}` }}>
            {["ID", "Patient", "Doctor", "Department", "Time", "Type", "Status"].map(h => (
              <th key={h} style={{ padding: "8px 10px", textAlign: "left", color: C.textMuted, fontWeight: 500, fontSize: 11, textTransform: "uppercase" }}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {MOCK.appointments.map(a => (
            <tr key={a.id} style={{ borderBottom: `1px solid ${C.border}` }}>
              <td style={{ padding: "10px 10px", fontFamily: mono, color: C.textMuted, fontSize: 12 }}>{a.id}</td>
              <td style={{ padding: "10px 10px", color: C.textPrimary, fontWeight: 500 }}>{a.patient}</td>
              <td style={{ padding: "10px 10px", color: C.textSecondary }}>{a.doctor}</td>
              <td style={{ padding: "10px 10px", color: C.textMuted }}>{a.dept}</td>
              <td style={{ padding: "10px 10px", fontFamily: mono, fontSize: 12, color: C.textSecondary }}>{a.time}</td>
              <td style={{ padding: "10px 10px" }}><Badge color="gray">{a.type}</Badge></td>
              <td style={{ padding: "10px 10px" }}><Badge color={a.status === "confirmed" ? "green" : a.status === "checked-in" ? "blue" : a.status === "cancelled" ? "red" : "amber"}>{a.status}</Badge></td>
            </tr>
          ))}
        </tbody>
      </table>
    </Card>
  </div>
);

const GenericPage = ({ title, description }) => (
  <div style={{ animation: "slideIn 0.4s ease", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", minHeight: 400, gap: 16 }}>
    <div style={{ fontSize: 56 }}>🏗</div>
    <h2 style={{ fontSize: 22, fontWeight: 700, color: C.textPrimary }}>{title}</h2>
    <p style={{ fontSize: 14, color: C.textSecondary, textAlign: "center", maxWidth: 400 }}>{description || "This page is part of the QueueSenseAI platform. Full implementation connects to the backend API."}</p>
    <div style={{ display: "flex", gap: 10 }}>
      <Badge color="cyan">Static Preview</Badge>
      <Badge color="purple">API-Ready</Badge>
    </div>
  </div>
);

// ─── Main App ──────────────────────────────────────────────────────────────────
export default function App() {
  const [role, setRole] = useState("Hospital Admin");
  const [page, setPage] = useState("ha-dash");
  const [notifOpen, setNotifOpen] = useState(false);
  const [sideOpen, setSideOpen] = useState(true);
  const [landing, setLanding] = useState(true);
  const [authPage, setAuthPage] = useState("login");
  const [showAuth, setShowAuth] = useState(false);
  const unread = MOCK.notifications.filter(n => !n.read).length;

  const handleRoleChange = (r) => {
    setRole(r);
    const pages = PAGES[r];
    setPage(pages[0].key);
    setLanding(false);
    setShowAuth(false);
  };

  const renderPage = () => {
    if (page === "sa-dash") return <SuperAdminDash />;
    if (page === "ha-dash") return <HospitalAdminDash />;
    if (page === "dr-dash") return <DoctorDash />;
    if (page === "pt-dash") return <PatientDash />;
    if (page === "st-dash") return <StaffDash />;
    if (page === "sa-ai" || page === "ha-queues") return <AIPage />;
    if (page === "ha-reports") return <ReportsPage />;
    if (page === "sa-hospitals") return <HospitalsPage />;
    if (page === "sa-subscriptions") return <SubscriptionsPage />;
    if (page === "sa-users") return <UsersPage />;
    if (page === "pt-track") return <PatientQueueTracking />;
    if (page === "pt-book") return <BookAppointment />;
    if (page === "dr-appointments") return <DoctorAppointments />;
    if (page === "st-emergency") return <EmergencyPage />;
    if (page === "dr-queue") return <AIPage />;
    return <GenericPage title={PAGES[role]?.find(p => p.key === page)?.label || "Page"} />;
  };

  if (landing) return <LandingPage onGetStarted={() => setShowAuth(true)} showAuth={showAuth} onLogin={handleRoleChange} />;

  return (
    <div style={{ display: "flex", height: "100vh", overflow: "hidden", background: C.navy, fontFamily: font }}>
      <style>{globalStyle}</style>

      {/* Sidebar */}
      <aside style={{ width: sideOpen ? 240 : 64, background: C.navyMid, borderRight: `1px solid ${C.border}`, display: "flex", flexDirection: "column", transition: "width 0.3s ease", overflow: "hidden", flexShrink: 0 }}>
        {/* Logo */}
        <div style={{ padding: "18px 16px", borderBottom: `1px solid ${C.border}`, display: "flex", alignItems: "center", gap: 10, minHeight: 64 }}>
          <div style={{ width: 32, height: 32, borderRadius: 8, background: C.cyan, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 16, flexShrink: 0, color: C.navy, fontWeight: 800 }}>Q</div>
          {sideOpen && <div><div style={{ fontSize: 14, fontWeight: 800, color: C.textPrimary, letterSpacing: "-0.02em" }}>QueueSense</div><div style={{ fontSize: 10, color: C.cyan, fontFamily: mono }}>AI</div></div>}
        </div>

        {/* Role badge */}
        {sideOpen && (
          <div style={{ padding: "10px 14px", margin: "10px 10px 4px", background: C.cyanGlow, border: `1px solid rgba(6,214,160,0.2)`, borderRadius: 8, fontSize: 11, color: C.cyan, fontWeight: 600 }}>
            {role}
          </div>
        )}

        {/* Nav items */}
        <nav style={{ flex: 1, padding: "8px 8px", overflowY: "auto" }}>
          {(PAGES[role] || []).map(item => (
            <button key={item.key} onClick={() => setPage(item.key)} style={{ width: "100%", display: "flex", alignItems: "center", gap: 10, padding: "9px 10px", borderRadius: 8, border: "none", cursor: "pointer", background: page === item.key ? C.cyanGlow : "transparent", color: page === item.key ? C.cyan : C.textSecondary, fontSize: 13, fontWeight: page === item.key ? 600 : 400, fontFamily: font, transition: "all 0.2s", marginBottom: 2, textAlign: "left", borderLeft: page === item.key ? `2px solid ${C.cyan}` : "2px solid transparent" }}>
              <span style={{ fontSize: 16, flexShrink: 0 }}>{item.icon}</span>
              {sideOpen && item.label}
            </button>
          ))}
        </nav>

        {/* Switch role */}
        {sideOpen && (
          <div style={{ padding: "12px", borderTop: `1px solid ${C.border}` }}>
            <div style={{ fontSize: 10, color: C.textMuted, marginBottom: 6, textTransform: "uppercase", letterSpacing: "0.08em" }}>Switch Role</div>
            <div style={{ display: "flex", flexDirection: "column", gap: 4 }}>
              {NAV_ROLES.map(r => (
                <button key={r} onClick={() => handleRoleChange(r)} style={{ padding: "6px 10px", borderRadius: 6, border: `1px solid ${r === role ? "rgba(6,214,160,0.3)" : C.border}`, background: r === role ? C.cyanGlow : "transparent", color: r === role ? C.cyan : C.textMuted, fontSize: 11, cursor: "pointer", fontFamily: font, textAlign: "left", transition: "all 0.2s" }}>
                  {r}
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Collapse */}
        <button onClick={() => setSideOpen(!sideOpen)} style={{ padding: 12, background: "transparent", border: "none", borderTop: `1px solid ${C.border}`, color: C.textMuted, cursor: "pointer", fontSize: 16, display: "flex", justifyContent: "center" }}>
          {sideOpen ? "◀" : "▶"}
        </button>
      </aside>

      {/* Main content */}
      <div style={{ flex: 1, display: "flex", flexDirection: "column", overflow: "hidden" }}>
        {/* Topbar */}
        <header style={{ height: 64, background: C.navyMid, borderBottom: `1px solid ${C.border}`, display: "flex", alignItems: "center", padding: "0 24px", gap: 16, flexShrink: 0 }}>
          <div style={{ flex: 1, display: "flex", alignItems: "center", gap: 12 }}>
            <h1 style={{ fontSize: 16, fontWeight: 700, color: C.textPrimary }}>
              {PAGES[role]?.find(p => p.key === page)?.label || "Dashboard"}
            </h1>
            <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
              <LiveDot />
              <span style={{ fontSize: 11, color: C.textMuted, fontFamily: mono }}>LIVE</span>
            </div>
          </div>

          {/* Search */}
          <div style={{ display: "flex", alignItems: "center", gap: 8, background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 8, padding: "6px 12px", width: 220 }}>
            <span style={{ color: C.textMuted, fontSize: 14 }}>🔍</span>
            <input placeholder="Search..." style={{ background: "transparent", border: "none", outline: "none", color: C.textPrimary, fontSize: 13, fontFamily: font, width: "100%" }} />
          </div>

          {/* Notifications */}
          <div style={{ position: "relative" }}>
            <button onClick={() => setNotifOpen(!notifOpen)} style={{ width: 36, height: 36, borderRadius: 8, background: C.cardBg, border: `1px solid ${C.border}`, display: "flex", alignItems: "center", justifyContent: "center", cursor: "pointer", fontSize: 16, color: C.textSecondary, position: "relative" }}>
              🔔
              {unread > 0 && <span style={{ position: "absolute", top: -4, right: -4, width: 16, height: 16, borderRadius: "50%", background: C.red, color: "#fff", fontSize: 9, fontWeight: 700, display: "flex", alignItems: "center", justifyContent: "center" }}>{unread}</span>}
            </button>
            {notifOpen && (
              <div style={{ position: "absolute", right: 0, top: 44, width: 340, background: C.navyMid, border: `1px solid ${C.border}`, borderRadius: 12, boxShadow: "0 20px 40px rgba(0,0,0,0.4)", zIndex: 100, overflow: "hidden", animation: "slideIn 0.2s ease" }}>
                <div style={{ padding: "14px 16px", borderBottom: `1px solid ${C.border}`, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                  <span style={{ fontWeight: 700, fontSize: 14, color: C.textPrimary }}>Notifications</span>
                  <Badge color="red">{unread} new</Badge>
                </div>
                <div style={{ maxHeight: 360, overflowY: "auto" }}>
                  {MOCK.notifications.map(n => (
                    <div key={n.id} style={{ padding: "12px 16px", borderBottom: `1px solid ${C.border}`, background: !n.read ? "rgba(255,255,255,0.03)" : "transparent" }}>
                      <div style={{ fontSize: 12, fontWeight: 600, color: n.type === "emergency" ? "#f87171" : n.type === "ai" ? C.purple : C.textPrimary, marginBottom: 3 }}>{n.title}</div>
                      <div style={{ fontSize: 11, color: C.textSecondary, marginBottom: 4, lineHeight: 1.5 }}>{n.body}</div>
                      <div style={{ fontSize: 10, color: C.textMuted }}>{n.time}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Avatar */}
          <div style={{ width: 36, height: 36, borderRadius: "50%", background: C.cyanGlow, border: `2px solid ${C.cyan}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 16, cursor: "pointer" }}>
            {role === "Doctor" ? "👨‍⚕️" : role === "Patient" ? "🙂" : role === "Staff" ? "👷" : "👤"}
          </div>

          <button onClick={() => setLanding(true)} style={{ padding: "6px 12px", background: "transparent", border: `1px solid ${C.border}`, borderRadius: 8, color: C.textMuted, cursor: "pointer", fontSize: 12, fontFamily: font }}>
            ← Home
          </button>
        </header>

        {/* Page content */}
        <main style={{ flex: 1, overflowY: "auto", padding: 24 }} onClick={() => notifOpen && setNotifOpen(false)}>
          {renderPage()}
        </main>
      </div>
    </div>
  );
}

// ─── Extra Pages ───────────────────────────────────────────────────────────────
const HospitalsPage = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <SectionHeader title="Hospital Network" sub="Manage all registered hospitals" action={<Btn variant="primary">+ Add Hospital</Btn>} />
    <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 16, marginBottom: 24 }}>
      <StatCard label="Total Hospitals" value="5" icon="🏥" />
      <StatCard label="Active" value="5" color={C.cyan} icon="✅" />
      <StatCard label="On Trial" value="1" color={C.amber} icon="🔄" />
    </div>
    <Card>
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
        <thead>
          <tr style={{ borderBottom: `1px solid ${C.border}` }}>
            {["Hospital", "City", "Patients Today", "Plan", "Status", "Health Score", "Actions"].map(h => (
              <th key={h} style={{ padding: "8px 10px", textAlign: "left", color: C.textMuted, fontWeight: 500, fontSize: 11, textTransform: "uppercase" }}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {MOCK.hospitals.map(h => (
            <tr key={h.id} style={{ borderBottom: `1px solid ${C.border}` }}>
              <td style={{ padding: "14px 10px", fontWeight: 600, color: C.textPrimary }}>{h.name}</td>
              <td style={{ padding: "14px 10px", color: C.textSecondary }}>{h.city}</td>
              <td style={{ padding: "14px 10px", fontFamily: mono, color: C.cyan }}>{h.patients.toLocaleString()}</td>
              <td style={{ padding: "14px 10px" }}><Badge color={h.plan === "Enterprise" ? "purple" : h.plan === "Pro" ? "blue" : "gray"}>{h.plan}</Badge></td>
              <td style={{ padding: "14px 10px" }}><Badge color="green" pulse>Active</Badge></td>
              <td style={{ padding: "14px 10px" }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  <div style={{ flex: 1, height: 4, background: C.border, borderRadius: 2 }}>
                    <div style={{ width: `${h.score}%`, height: "100%", background: C.cyan, borderRadius: 2 }} />
                  </div>
                  <span style={{ fontFamily: mono, fontSize: 11, color: C.textSecondary }}>{h.score}%</span>
                </div>
              </td>
              <td style={{ padding: "14px 10px" }}>
                <div style={{ display: "flex", gap: 6 }}>
                  <Btn variant="ghost" size="sm">View</Btn>
                  <Btn variant="cyan" size="sm">Edit</Btn>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Card>
  </div>
);

const SubscriptionsPage = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <SectionHeader title="Subscription & Billing" sub="Manage plans, revenue and transactions" />
    <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 16, marginBottom: 24 }}>
      <StatCard label="MRR" value="₹24.8L" color={C.cyan} icon="💰" trend={12} />
      <StatCard label="ARR" value="₹2.97Cr" color={C.purple} icon="📈" trend={18} />
      <StatCard label="Active Subs" value="5" icon="✅" />
      <StatCard label="Churn Rate" value="0%" color={C.amber} icon="🔄" />
    </div>
    <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 20 }}>
      {[
        { name: "Starter", price: "₹9,999/mo", features: ["1 Hospital", "Up to 3 Doctors", "Basic Queue", "Email Support"], color: C.textMuted, hospitals: 1 },
        { name: "Pro", price: "₹29,999/mo", features: ["1 Hospital", "Up to 20 Doctors", "AI Queue Mgmt", "Priority Support", "Analytics"], color: C.blue, hospitals: 2, recommended: true },
        { name: "Enterprise", price: "₹79,999/mo", features: ["Multi-Hospital", "Unlimited Doctors", "Full AI Suite", "Dedicated CSM", "Custom Integrations"], color: C.purple, hospitals: 2 },
      ].map(p => (
        <Card key={p.name} style={{ border: p.recommended ? `2px solid ${C.cyan}` : `1px solid ${C.border}` }}>
          {p.recommended && <div style={{ marginBottom: 10 }}><Badge color="green">Most Popular</Badge></div>}
          <div style={{ fontSize: 18, fontWeight: 800, color: p.color, marginBottom: 4 }}>{p.name}</div>
          <div style={{ fontSize: 24, fontWeight: 700, color: C.textPrimary, fontFamily: mono, marginBottom: 16 }}>{p.price}</div>
          <div style={{ display: "flex", flexDirection: "column", gap: 6, marginBottom: 16 }}>
            {p.features.map(f => (
              <div key={f} style={{ fontSize: 12, color: C.textSecondary, display: "flex", alignItems: "center", gap: 6 }}>
                <span style={{ color: C.cyan }}>✓</span> {f}
              </div>
            ))}
          </div>
          <div style={{ fontSize: 12, color: C.textMuted, marginBottom: 12 }}>{p.hospitals} hospital{p.hospitals > 1 ? "s" : ""} on this plan</div>
          <Btn variant={p.recommended ? "primary" : "ghost"} size="md" style={{ width: "100%" }}>Manage Plan</Btn>
        </Card>
      ))}
    </div>
  </div>
);

const UsersPage = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <SectionHeader title="User Management" sub="All platform users across roles" action={<Btn variant="primary">+ Create User</Btn>} />
    <div style={{ display: "grid", gridTemplateColumns: "repeat(5,1fr)", gap: 14, marginBottom: 24 }}>
      {[
        { role: "Super Admins", count: 2, color: C.red, icon: "👑" },
        { role: "Hospital Admins", count: 8, color: C.purple, icon: "🏥" },
        { role: "Doctors", count: 142, color: C.blue, icon: "👨‍⚕️" },
        { role: "Staff", count: 67, color: C.cyan, icon: "👷" },
        { role: "Patients", count: 9400, color: C.amber, icon: "🫀" },
      ].map(u => (
        <Card key={u.role} style={{ textAlign: "center" }}>
          <div style={{ fontSize: 28, marginBottom: 8 }}>{u.icon}</div>
          <div style={{ fontSize: 28, fontWeight: 800, fontFamily: mono, color: u.color }}>{u.count.toLocaleString()}</div>
          <div style={{ fontSize: 12, color: C.textMuted, marginTop: 4 }}>{u.role}</div>
        </Card>
      ))}
    </div>
    <Card>
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
        <thead>
          <tr style={{ borderBottom: `1px solid ${C.border}` }}>
            {["Name", "Email", "Role", "Hospital", "Last Active", "Status", "Actions"].map(h => (
              <th key={h} style={{ padding: "8px 10px", textAlign: "left", color: C.textMuted, fontWeight: 500, fontSize: 11, textTransform: "uppercase" }}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {[
            { name: "Dr. Priya Sharma", email: "priya@aiims.in", role: "Doctor", hospital: "AIIMS Delhi", last: "2 min ago", status: "active" },
            { name: "Admin Rajesh", email: "rajesh@fortis.in", role: "Hospital Admin", hospital: "Fortis Mumbai", last: "1 hr ago", status: "active" },
            { name: "Nurse Kavitha", email: "kavitha@apollo.in", role: "Staff", hospital: "Apollo Chennai", last: "30 min ago", status: "active" },
            { name: "Ravi Shankar", email: "ravi@gmail.com", role: "Patient", hospital: "AIIMS Delhi", last: "10 min ago", status: "active" },
            { name: "Dr. Vikram Singh", email: "vikram@medanta.in", role: "Doctor", hospital: "Medanta Gurugram", last: "Yesterday", status: "inactive" },
          ].map((u, i) => (
            <tr key={i} style={{ borderBottom: `1px solid ${C.border}` }}>
              <td style={{ padding: "12px 10px", fontWeight: 600, color: C.textPrimary }}>{u.name}</td>
              <td style={{ padding: "12px 10px", color: C.textMuted, fontSize: 12 }}>{u.email}</td>
              <td style={{ padding: "12px 10px" }}><Badge color={u.role === "Doctor" ? "blue" : u.role === "Hospital Admin" ? "purple" : u.role === "Staff" ? "cyan" : "gray"}>{u.role}</Badge></td>
              <td style={{ padding: "12px 10px", color: C.textSecondary, fontSize: 12 }}>{u.hospital}</td>
              <td style={{ padding: "12px 10px", color: C.textMuted, fontSize: 12, fontFamily: mono }}>{u.last}</td>
              <td style={{ padding: "12px 10px" }}><Badge color={u.status === "active" ? "green" : "gray"}>{u.status}</Badge></td>
              <td style={{ padding: "12px 10px" }}>
                <div style={{ display: "flex", gap: 6 }}>
                  <Btn variant="ghost" size="sm">Edit</Btn>
                  <Btn variant="danger" size="sm">Disable</Btn>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Card>
  </div>
);

const PatientQueueTracking = () => {
  const [pos, setPos] = useState(3);
  useEffect(() => {
    const t = setInterval(() => setPos(p => Math.max(1, p)), 5000);
    return () => clearInterval(t);
  }, []);

  return (
    <div style={{ animation: "slideIn 0.4s ease", maxWidth: 700, margin: "0 auto" }}>
      <Card style={{ textAlign: "center", marginBottom: 20, background: "rgba(6,214,160,0.05)", border: "1px solid rgba(6,214,160,0.25)" }}>
        <div style={{ fontSize: 12, color: C.cyan, fontWeight: 700, letterSpacing: "0.1em", marginBottom: 16 }}>LIVE QUEUE TRACKING</div>
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 6, marginBottom: 8 }}>
          <LiveDot />
          <span style={{ fontSize: 13, color: C.textSecondary }}>Your token is active</span>
        </div>
        <div style={{ fontSize: 72, fontWeight: 900, fontFamily: mono, color: C.cyan, lineHeight: 1 }}>A004</div>
        <div style={{ fontSize: 16, color: C.textSecondary, margin: "12px 0" }}>Cardiology • Dr. Priya Sharma</div>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 16, margin: "20px 0" }}>
          <div style={{ padding: 16, background: C.cardBgHover, borderRadius: 10 }}>
            <div style={{ fontSize: 11, color: C.textMuted, marginBottom: 6 }}>POSITION</div>
            <div style={{ fontSize: 36, fontWeight: 800, fontFamily: mono, color: C.textPrimary }}>#{pos}</div>
          </div>
          <div style={{ padding: 16, background: C.cardBgHover, borderRadius: 10 }}>
            <div style={{ fontSize: 11, color: C.textMuted, marginBottom: 6 }}>EST. WAIT</div>
            <div style={{ fontSize: 36, fontWeight: 800, fontFamily: mono, color: C.amber }}>{pos * 14}m</div>
          </div>
          <div style={{ padding: 16, background: C.cardBgHover, borderRadius: 10 }}>
            <div style={{ fontSize: 11, color: C.textMuted, marginBottom: 6 }}>AI ACCURACY</div>
            <div style={{ fontSize: 36, fontWeight: 800, fontFamily: mono, color: C.cyan }}>91%</div>
          </div>
        </div>
        <div style={{ padding: "10px 16px", background: "rgba(245,158,11,0.1)", border: "1px solid rgba(245,158,11,0.2)", borderRadius: 8, fontSize: 12, color: "#fbbf24" }}>
          ⚡ AI predicts a 2-patient callup spike in ~10 minutes. Wait may reduce sooner.
        </div>
      </Card>

      <Card>
        <SectionHeader title="Queue Ahead of You" />
        <div style={{ display: "flex", flexDirection: "column", gap: 6 }}>
          {["A001 — Ramesh Kumar (Consulting Now)", "A002 — Sunita Devi (~14 min)", "A003 — Mohan Lal (~28 min)", `A004 — You (~${pos * 14} min)`].map((t, i) => (
            <div key={i} style={{ display: "flex", alignItems: "center", gap: 10, padding: "10px 12px", background: i === 3 ? C.cyanGlow : i === 0 ? "rgba(6,214,160,0.08)" : "transparent", borderRadius: 8, border: `1px solid ${i === 3 ? "rgba(6,214,160,0.3)" : "transparent"}` }}>
              <div style={{ width: 8, height: 8, borderRadius: "50%", background: i === 0 ? C.cyan : i === 3 ? C.cyan : C.textMuted, flexShrink: 0 }} />
              <span style={{ fontSize: 13, color: i === 3 ? C.cyan : i === 0 ? C.textPrimary : C.textSecondary, fontFamily: mono, fontWeight: i === 3 ? 700 : 400 }}>{t}</span>
              {i === 3 && <Badge color="green" style={{ marginLeft: "auto" }}>You</Badge>}
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};

const BookAppointment = () => {
  const [step, setStep] = useState(1);
  const [selected, setSelected] = useState({ dept: "", doctor: "", slot: "" });

  return (
    <div style={{ animation: "slideIn 0.4s ease", maxWidth: 700, margin: "0 auto" }}>
      <div style={{ display: "flex", gap: 0, marginBottom: 24 }}>
        {["Select Department", "Choose Doctor", "Pick Slot", "Confirm"].map((s, i) => (
          <div key={i} style={{ flex: 1, display: "flex", flexDirection: "column", alignItems: "center", gap: 6 }}>
            <div style={{ width: 32, height: 32, borderRadius: "50%", background: step > i + 1 ? C.cyan : step === i + 1 ? C.cyanGlow : C.border, border: `2px solid ${step >= i + 1 ? C.cyan : C.border}`, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 13, fontWeight: 700, color: step > i + 1 ? C.navy : step === i + 1 ? C.cyan : C.textMuted }}>
              {step > i + 1 ? "✓" : i + 1}
            </div>
            <div style={{ fontSize: 10, color: step === i + 1 ? C.cyan : C.textMuted, textAlign: "center" }}>{s}</div>
          </div>
        ))}
      </div>

      <Card>
        {step === 1 && (
          <div>
            <SectionHeader title="Select Department" />
            <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 10 }}>
              {["Cardiology", "Neurology", "Orthopedics", "Dermatology", "Pediatrics", "General Medicine"].map(d => (
                <button key={d} onClick={() => { setSelected({ ...selected, dept: d }); setStep(2); }} style={{ padding: "14px", background: selected.dept === d ? C.cyanGlow : C.cardBgHover, border: `1px solid ${selected.dept === d ? "rgba(6,214,160,0.4)" : C.border}`, borderRadius: 10, color: selected.dept === d ? C.cyan : C.textSecondary, cursor: "pointer", fontSize: 13, fontWeight: 500, fontFamily: font, transition: "all 0.2s" }}>
                  {d}
                </button>
              ))}
            </div>
          </div>
        )}
        {step === 2 && (
          <div>
            <SectionHeader title={`Doctors — ${selected.dept}`} action={<Btn variant="ghost" size="sm" onClick={() => setStep(1)}>← Back</Btn>} />
            <div style={{ display: "flex", flexDirection: "column", gap: 10 }}>
              {MOCK.doctors.filter(d => d.dept === selected.dept || true).slice(0, 3).map(d => (
                <button key={d.id} onClick={() => { setSelected({ ...selected, doctor: d.name }); setStep(3); }} style={{ display: "flex", alignItems: "center", gap: 12, padding: "14px", background: C.cardBgHover, border: `1px solid ${C.border}`, borderRadius: 10, cursor: "pointer", textAlign: "left", fontFamily: font, transition: "all 0.2s" }}>
                  <div style={{ width: 40, height: 40, borderRadius: "50%", background: "rgba(59,130,246,0.15)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 20 }}>👨‍⚕️</div>
                  <div style={{ flex: 1 }}>
                    <div style={{ fontSize: 14, fontWeight: 600, color: C.textPrimary }}>{d.name}</div>
                    <div style={{ fontSize: 12, color: C.textSecondary }}>{d.dept} • Avg {d.avg}</div>
                  </div>
                  <Badge color={d.status === "available" ? "green" : "amber"}>{d.status}</Badge>
                </button>
              ))}
            </div>
          </div>
        )}
        {step === 3 && (
          <div>
            <SectionHeader title="Available Slots" action={<Btn variant="ghost" size="sm" onClick={() => setStep(2)}>← Back</Btn>} />
            <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 8 }}>
              {["9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "2:00 PM", "2:30 PM"].map(slot => (
                <button key={slot} onClick={() => { setSelected({ ...selected, slot }); setStep(4); }} style={{ padding: "10px", background: selected.slot === slot ? C.cyanGlow : C.cardBgHover, border: `1px solid ${selected.slot === slot ? "rgba(6,214,160,0.4)" : C.border}`, borderRadius: 8, color: selected.slot === slot ? C.cyan : C.textSecondary, cursor: "pointer", fontFamily: mono, fontSize: 13, transition: "all 0.2s" }}>
                  {slot}
                </button>
              ))}
            </div>
          </div>
        )}
        {step === 4 && (
          <div style={{ textAlign: "center" }}>
            <div style={{ fontSize: 48, marginBottom: 16 }}>✅</div>
            <h3 style={{ fontSize: 20, fontWeight: 700, color: C.textPrimary, marginBottom: 8 }}>Appointment Confirmed!</h3>
            <div style={{ padding: "16px", background: C.cardBgHover, borderRadius: 10, marginBottom: 20, textAlign: "left" }}>
              <div style={{ display: "flex", flexDirection: "column", gap: 8, fontSize: 13 }}>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <span style={{ color: C.textMuted }}>Department</span><span style={{ color: C.textPrimary }}>{selected.dept || "Cardiology"}</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <span style={{ color: C.textMuted }}>Doctor</span><span style={{ color: C.textPrimary }}>{selected.doctor || "Dr. Priya Sharma"}</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <span style={{ color: C.textMuted }}>Slot</span><span style={{ color: C.cyan, fontFamily: mono }}>{selected.slot || "10:00 AM"}</span>
                </div>
                <div style={{ display: "flex", justifyContent: "space-between" }}>
                  <span style={{ color: C.textMuted }}>Token</span><span style={{ color: C.cyan, fontFamily: mono }}>A007</span>
                </div>
              </div>
            </div>
            <Btn variant="primary" size="lg" onClick={() => setStep(1)}>Book Another</Btn>
          </div>
        )}
      </Card>
    </div>
  );
};

const DoctorAppointments = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <SectionHeader title="Today's Appointments" sub="12 May 2025 — Cardiology" />
    <Card>
      <table style={{ width: "100%", borderCollapse: "collapse", fontSize: 13 }}>
        <thead>
          <tr style={{ borderBottom: `1px solid ${C.border}` }}>
            {["Token", "Patient", "Time", "Type", "Status", "Action"].map(h => (
              <th key={h} style={{ padding: "8px 10px", textAlign: "left", color: C.textMuted, fontWeight: 500, fontSize: 11, textTransform: "uppercase" }}>{h}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {MOCK.appointments.map(a => (
            <tr key={a.id} style={{ borderBottom: `1px solid ${C.border}` }}>
              <td style={{ padding: "12px 10px", fontFamily: mono, color: C.cyan }}>{a.id.replace("APT", "A0")}</td>
              <td style={{ padding: "12px 10px", fontWeight: 600, color: C.textPrimary }}>{a.patient}</td>
              <td style={{ padding: "12px 10px", fontFamily: mono, color: C.textSecondary, fontSize: 12 }}>{a.time}</td>
              <td style={{ padding: "12px 10px" }}><Badge color="gray">{a.type}</Badge></td>
              <td style={{ padding: "12px 10px" }}><Badge color={a.status === "confirmed" ? "green" : a.status === "checked-in" ? "blue" : a.status === "cancelled" ? "red" : "amber"}>{a.status}</Badge></td>
              <td style={{ padding: "12px 10px" }}>
                <div style={{ display: "flex", gap: 6 }}>
                  <Btn variant="cyan" size="sm">View</Btn>
                  <Btn variant="ghost" size="sm">Notes</Btn>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </Card>
  </div>
);

const EmergencyPage = () => (
  <div style={{ animation: "slideIn 0.4s ease" }}>
    <div style={{ padding: "14px 18px", background: "rgba(239,68,68,0.08)", border: "1px solid rgba(239,68,68,0.3)", borderRadius: 12, marginBottom: 24, display: "flex", alignItems: "center", gap: 12 }}>
      <span style={{ fontSize: 24, animation: "pulse 1s ease-in-out infinite" }}>🚨</span>
      <div>
        <div style={{ fontSize: 16, fontWeight: 700, color: "#f87171" }}>Emergency Handling Mode</div>
        <div style={{ fontSize: 12, color: C.textSecondary }}>2 active emergency cases — immediate attention required</div>
      </div>
      <Btn variant="danger" size="sm" style={{ marginLeft: "auto" }}>Trigger Code Blue</Btn>
    </div>

    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 20 }}>
      {[
        { name: "Anjali Singh", age: 34, condition: "Chest Pain — Suspected MI", bp: "160/100", hr: "110", spo2: "92%", time: "2 min ago", severity: "critical" },
        { name: "Ramesh Yadav", age: 68, condition: "Stroke Symptoms — Slurred speech", bp: "180/110", hr: "95", spo2: "96%", time: "14 min ago", severity: "critical" },
      ].map((e, i) => (
        <Card key={i} style={{ background: "rgba(239,68,68,0.05)", border: "1px solid rgba(239,68,68,0.3)" }}>
          <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 12 }}>
            <Badge color="red" pulse>CRITICAL</Badge>
            <span style={{ fontSize: 11, color: C.textMuted, fontFamily: mono }}>{e.time}</span>
          </div>
          <div style={{ fontSize: 18, fontWeight: 700, color: C.textPrimary, marginBottom: 4 }}>{e.name}, {e.age}y</div>
          <div style={{ fontSize: 13, color: "#f87171", marginBottom: 16 }}>{e.condition}</div>
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 10, marginBottom: 16 }}>
            {[["BP", e.bp], ["HR", e.hr], ["SpO2", e.spo2]].map(([k, v]) => (
              <div key={k} style={{ padding: "8px 10px", background: C.cardBgHover, borderRadius: 8, textAlign: "center" }}>
                <div style={{ fontSize: 10, color: C.textMuted, marginBottom: 4 }}>{k}</div>
                <div style={{ fontSize: 16, fontWeight: 700, fontFamily: mono, color: k === "SpO2" && parseInt(v) < 95 ? C.red : C.textPrimary }}>{v}</div>
              </div>
            ))}
          </div>
          <div style={{ display: "flex", gap: 8 }}>
            <Btn variant="danger" size="md" style={{ flex: 1 }}>Assign Doctor</Btn>
            <Btn variant="ghost" size="md">Escalate</Btn>
            <Btn variant="ghost" size="md">Notes</Btn>
          </div>
        </Card>
      ))}
    </div>
  </div>
);

// ─── Landing Page ──────────────────────────────────────────────────────────────
const LandingPage = ({ onGetStarted, showAuth, onLogin }) => {
  const [authTab, setAuthTab] = useState("login");
  const [selectedRole, setSelectedRole] = useState("");

  if (showAuth) {
    return (
      <div style={{ minHeight: "100vh", background: C.navy, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: font }}>
        <style>{globalStyle}</style>
        <div style={{ width: 420, animation: "slideIn 0.4s ease" }}>
          <div style={{ textAlign: "center", marginBottom: 32 }}>
            <div style={{ width: 52, height: 52, borderRadius: 14, background: C.cyan, display: "flex", alignItems: "center", justifyContent: "center", fontSize: 26, margin: "0 auto 16px", color: C.navy, fontWeight: 900 }}>Q</div>
            <h1 style={{ fontSize: 26, fontWeight: 800, color: C.textPrimary, marginBottom: 6 }}>QueueSense AI</h1>
            <p style={{ fontSize: 13, color: C.textSecondary }}>Intelligent hospital queue management</p>
          </div>

          <Card>
            <div style={{ display: "flex", gap: 0, marginBottom: 24, background: C.border, borderRadius: 8, padding: 3 }}>
              {["login", "register"].map(t => (
                <button key={t} onClick={() => setAuthTab(t)} style={{ flex: 1, padding: "8px", borderRadius: 6, border: "none", background: authTab === t ? C.navyLight : "transparent", color: authTab === t ? C.textPrimary : C.textMuted, cursor: "pointer", fontFamily: font, fontSize: 13, fontWeight: authTab === t ? 600 : 400 }}>
                  {t === "login" ? "Sign In" : "Register"}
                </button>
              ))}
            </div>

            {authTab === "login" ? (
              <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
                <div>
                  <label style={{ fontSize: 12, color: C.textSecondary, display: "block", marginBottom: 6 }}>Email</label>
                  <input defaultValue="admin@aiims.in" style={{ width: "100%", padding: "10px 12px", background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 8, color: C.textPrimary, fontSize: 13, fontFamily: font, outline: "none" }} />
                </div>
                <div>
                  <label style={{ fontSize: 12, color: C.textSecondary, display: "block", marginBottom: 6 }}>Password</label>
                  <input type="password" defaultValue="••••••••" style={{ width: "100%", padding: "10px 12px", background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 8, color: C.textPrimary, fontSize: 13, fontFamily: font, outline: "none" }} />
                </div>
                <div>
                  <label style={{ fontSize: 12, color: C.textSecondary, display: "block", marginBottom: 6 }}>Login As</label>
                  <select onChange={e => setSelectedRole(e.target.value)} style={{ width: "100%", padding: "10px 12px", background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 8, color: C.textPrimary, fontSize: 13, fontFamily: font, outline: "none" }}>
                    <option value="">Select role…</option>
                    {NAV_ROLES.map(r => <option key={r} value={r}>{r}</option>)}
                  </select>
                </div>
                <Btn variant="primary" size="lg" style={{ width: "100%", marginTop: 6 }} onClick={() => onLogin(selectedRole || "Hospital Admin")}>
                  Sign In →
                </Btn>
                <div style={{ textAlign: "center", fontSize: 12, color: C.textMuted }}>Demo: select any role and sign in</div>
              </div>
            ) : (
              <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
                {["Full Name", "Email", "Hospital / Organization", "Phone"].map(f => (
                  <div key={f}>
                    <label style={{ fontSize: 12, color: C.textSecondary, display: "block", marginBottom: 6 }}>{f}</label>
                    <input placeholder={f} style={{ width: "100%", padding: "10px 12px", background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 8, color: C.textPrimary, fontSize: 13, fontFamily: font, outline: "none" }} />
                  </div>
                ))}
                <Btn variant="primary" size="lg" style={{ width: "100%", marginTop: 6 }} onClick={() => onLogin("Hospital Admin")}>
                  Register & Continue →
                </Btn>
              </div>
            )}
          </Card>
        </div>
      </div>
    );
  }

  return (
    <div style={{ minHeight: "100vh", background: C.navy, fontFamily: font, overflowX: "hidden" }}>
      <style>{globalStyle}</style>

      {/* Nav */}
      <nav style={{ padding: "0 60px", height: 64, display: "flex", alignItems: "center", borderBottom: `1px solid ${C.border}`, position: "sticky", top: 0, background: "rgba(11,17,32,0.95)", backdropFilter: "blur(12px)", zIndex: 50 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <div style={{ width: 32, height: 32, borderRadius: 8, background: C.cyan, display: "flex", alignItems: "center", justifyContent: "center", color: C.navy, fontWeight: 900, fontSize: 16 }}>Q</div>
          <span style={{ fontSize: 17, fontWeight: 800, color: C.textPrimary }}>QueueSense</span>
          <span style={{ fontSize: 12, color: C.cyan, fontFamily: mono, marginLeft: 2 }}>AI</span>
        </div>
        <div style={{ display: "flex", gap: 28, marginLeft: 48 }}>
          {["Features", "Pricing", "About", "Contact"].map(l => (
            <a key={l} href="#" style={{ fontSize: 13, color: C.textSecondary, textDecoration: "none" }}>{l}</a>
          ))}
        </div>
        <div style={{ marginLeft: "auto", display: "flex", gap: 10 }}>
          <Btn variant="ghost" size="sm" onClick={onGetStarted}>Sign In</Btn>
          <Btn variant="primary" size="sm" onClick={onGetStarted}>Get Started</Btn>
        </div>
      </nav>

      {/* Hero */}
      <section style={{ padding: "80px 60px 60px", textAlign: "center", maxWidth: 900, margin: "0 auto" }}>
        <div style={{ display: "inline-flex", alignItems: "center", gap: 8, padding: "5px 14px", background: C.cyanGlow, border: `1px solid rgba(6,214,160,0.3)`, borderRadius: 20, fontSize: 12, color: C.cyan, fontWeight: 600, marginBottom: 24 }}>
          <LiveDot />
          AI-Powered Queue Management — Now Available
        </div>
        <h1 style={{ fontSize: 58, fontWeight: 900, color: C.textPrimary, lineHeight: 1.1, marginBottom: 20, letterSpacing: "-0.03em" }}>
          No more waiting.<br />
          <span style={{ color: C.cyan }}>Smarter</span> hospital queues.
        </h1>
        <p style={{ fontSize: 17, color: C.textSecondary, lineHeight: 1.7, marginBottom: 36, maxWidth: 580, margin: "0 auto 36px" }}>
          QueueSenseAI uses real-time AI to predict queue loads, minimize patient wait times, and give doctors, staff, and patients full visibility — all in one platform.
        </p>
        <div style={{ display: "flex", gap: 12, justifyContent: "center" }}>
          <Btn variant="primary" size="lg" onClick={onGetStarted}>Start Free Trial →</Btn>
          <Btn variant="ghost" size="lg">Watch Demo</Btn>
        </div>

        {/* Stats */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(4,1fr)", gap: 20, marginTop: 60, padding: "28px 32px", background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 16 }}>
          {[
            { label: "Avg Wait Reduction", value: "42%", color: C.cyan },
            { label: "Hospitals Served", value: "120+", color: C.purple },
            { label: "Patients Managed", value: "2.4M", color: C.blue },
            { label: "AI Accuracy", value: "94.7%", color: C.amber },
          ].map(s => (
            <div key={s.label} style={{ textAlign: "center" }}>
              <div style={{ fontSize: 36, fontWeight: 900, fontFamily: mono, color: s.color }}>{s.value}</div>
              <div style={{ fontSize: 12, color: C.textMuted, marginTop: 4 }}>{s.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* Features */}
      <section style={{ padding: "60px 60px", background: C.navyMid }}>
        <h2 style={{ fontSize: 32, fontWeight: 800, color: C.textPrimary, textAlign: "center", marginBottom: 8 }}>Everything you need. Nothing you don't.</h2>
        <p style={{ textAlign: "center", color: C.textSecondary, fontSize: 15, marginBottom: 48 }}>Built for hospitals of every scale — from clinics to multi-facility networks.</p>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(3,1fr)", gap: 20, maxWidth: 1100, margin: "0 auto" }}>
          {[
            { icon: "🤖", title: "AI Queue Prediction", body: "ML models trained on millions of patient records forecast queue peaks and wait times in real-time.", color: C.purple },
            { icon: "🚨", title: "Emergency Prioritization", body: "Automatic triage detection elevates critical patients instantly — zero manual override needed.", color: C.red },
            { icon: "📍", title: "Live Queue Tracking", body: "Patients track their exact position and ETA on mobile. Instant SMS & push notifications.", color: C.cyan },
            { icon: "👨‍⚕️", title: "Doctor Dashboard", body: "Doctors see their full queue, consult history, and patient vitals in one clean interface.", color: C.blue },
            { icon: "📊", title: "Analytics & Reports", body: "Department-level performance reports, AI forecast accuracy, and revenue analytics.", color: C.amber },
            { icon: "🔔", title: "Smart Notifications", body: "Multi-channel alerts for patients, staff, and doctors — all orchestrated by the AI engine.", color: C.green },
          ].map(f => (
            <Card key={f.title} style={{ background: C.navy }}>
              <div style={{ fontSize: 32, marginBottom: 12 }}>{f.icon}</div>
              <h3 style={{ fontSize: 16, fontWeight: 700, color: C.textPrimary, marginBottom: 8 }}>{f.title}</h3>
              <p style={{ fontSize: 13, color: C.textSecondary, lineHeight: 1.6 }}>{f.body}</p>
            </Card>
          ))}
        </div>
      </section>

      {/* Roles */}
      <section style={{ padding: "60px", textAlign: "center" }}>
        <h2 style={{ fontSize: 32, fontWeight: 800, color: C.textPrimary, marginBottom: 8 }}>One platform, five roles</h2>
        <p style={{ color: C.textSecondary, fontSize: 15, marginBottom: 40 }}>Tailored experience for every stakeholder in the hospital</p>
        <div style={{ display: "flex", gap: 14, justifyContent: "center", flexWrap: "wrap" }}>
          {[
            { role: "Super Admin", icon: "👑", desc: "Full platform oversight, analytics, billing" },
            { role: "Hospital Admin", icon: "🏥", desc: "Queue control, staff, departments" },
            { role: "Doctor", icon: "👨‍⚕️", desc: "Appointments, queue, patient notes" },
            { role: "Staff", icon: "👷", desc: "Check-in, walk-in, emergency handling" },
            { role: "Patient", icon: "🫀", desc: "Booking, tracking, history, payments" },
          ].map(r => (
            <button key={r.role} onClick={() => onLogin(r.role)} style={{ padding: "20px 24px", background: C.cardBg, border: `1px solid ${C.border}`, borderRadius: 14, cursor: "pointer", textAlign: "center", transition: "all 0.2s", minWidth: 160, fontFamily: font }}>
              <div style={{ fontSize: 32, marginBottom: 10 }}>{r.icon}</div>
              <div style={{ fontSize: 14, fontWeight: 700, color: C.textPrimary, marginBottom: 6 }}>{r.role}</div>
              <div style={{ fontSize: 11, color: C.textMuted }}>{r.desc}</div>
              <div style={{ marginTop: 10 }}><Badge color="cyan">Preview →</Badge></div>
            </button>
          ))}
        </div>
      </section>

      {/* CTA */}
      <section style={{ padding: "60px", background: C.navyMid, textAlign: "center" }}>
        <h2 style={{ fontSize: 36, fontWeight: 900, color: C.textPrimary, marginBottom: 12 }}>Ready to eliminate the wait?</h2>
        <p style={{ color: C.textSecondary, fontSize: 15, marginBottom: 32 }}>Join 120+ hospitals using QueueSenseAI to deliver better patient experiences.</p>
        <Btn variant="primary" size="lg" onClick={onGetStarted}>Start Your Free 30-Day Trial →</Btn>
      </section>

      {/* Footer */}
      <footer style={{ padding: "32px 60px", borderTop: `1px solid ${C.border}`, display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <div style={{ width: 24, height: 24, borderRadius: 6, background: C.cyan, display: "flex", alignItems: "center", justifyContent: "center", color: C.navy, fontWeight: 900, fontSize: 13 }}>Q</div>
          <span style={{ fontSize: 13, fontWeight: 700, color: C.textSecondary }}>QueueSenseAI</span>
        </div>
        <div style={{ fontSize: 12, color: C.textMuted }}>© 2025 QueueSenseAI. Built for better healthcare.</div>
        <div style={{ display: "flex", gap: 16, fontSize: 12, color: C.textMuted }}>
          {["Privacy", "Terms", "Help", "Contact"].map(l => <a key={l} href="#" style={{ color: C.textMuted, textDecoration: "none" }}>{l}</a>)}
        </div>
      </footer>
    </div>
  );
};