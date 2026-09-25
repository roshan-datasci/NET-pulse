import { useEffect, useMemo, useState } from "react";
import "./index.css";

/* =========================================================
   TASKS
========================================================= */

const TASKS = [
  {
    id: "general",
    label: "General Usage",
  },
  {
    id: "browsing",
    label: "Web Browsing",
  },
  {
    id: "social_media",
    label: "Social & Streaming",
  },
  {
    id: "video_call",
    label: "Video Call",
  },
  {
    id: "download",
    label: "Large Downloads",
  },
  {
    id: "gaming",
    label: "Gaming",
  },
];

/* =========================================================
   DEMO NETWORK DATA
========================================================= */

const BASE_NETWORKS = [
  {
    name: "LibraryWing_5G",
    rssi: -58,
    speed: 87.4,
    status: "GOOD",
    distance: 14.5,
    direction: "North-East",
  },
  {
    name: "CourtYard_Open",
    rssi: -67,
    speed: 54.2,
    status: "GOOD",
    distance: 21.2,
    direction: "East",
  },
  {
    name: "AdminBlock_Secure",
    rssi: -74,
    speed: 31.8,
    status: "FAIR",
    distance: 28.4,
    direction: "South-East",
  },
];

/* =========================================================
   INITIAL LIVE TELEMETRY
========================================================= */

const INITIAL_TELEMETRY = {
  rssi: -92,
  speed: 2.1,
  latency: 284,
};

/* =========================================================
   UTILITY FUNCTIONS
========================================================= */

function clamp(value, minimum, maximum) {
  return Math.max(minimum, Math.min(maximum, value));
}

/*
  Convert RSSI into a simple 1–4 signal level.
*/
function getSignalLevel(rssi) {
  if (rssi >= -60) return 4;
  if (rssi >= -68) return 3;
  if (rssi >= -76) return 2;

  return 1;
}

/*
  Determine expected streaming quality from speed.
*/
function getVideoQuality(speed) {
  if (speed >= 50) {
    return "4K UHD";
  }

  if (speed >= 20) {
    return "1080p Full HD";
  }

  if (speed >= 8) {
    return "720p HD";
  }

  return "480p SD";
}

function getVideoLevel(speed) {
  if (speed >= 50) return 4;
  if (speed >= 20) return 3;
  if (speed >= 8) return 2;

  return 1;
}

/*
  Calculate download time.

  File size is GB.
  Speed is Mbps.
*/
function calculateDownloadTime(fileSizeGB, speedMbps) {
  const fileBits = fileSizeGB * 8 * 1024 * 1024 * 1024;

  const seconds =
    fileBits / (speedMbps * 1000 * 1000);

  return seconds;
}

function formatTime(seconds) {
  if (seconds < 60) {
    return `${Math.round(seconds)}s`;
  }

  const minutes = Math.floor(seconds / 60);

  const remainingSeconds =
    Math.round(seconds % 60);

  if (minutes >= 60) {
    const hours = Math.floor(minutes / 60);
    const remainingMinutes = minutes % 60;

    return `${hours}h ${remainingMinutes}m`;
  }

  return `${minutes}m ${remainingSeconds}s`;
}

function getStatusFromSpeed(speed) {
  if (speed >= 20) {
    return "GOOD";
  }

  return "FAIR";
}

/* =========================================================
   SIGNAL BARS
========================================================= */

function SignalBars({ rssi }) {
  const bars = getSignalLevel(rssi);

  return (
    <div className="signal-bars">
      {[1, 2, 3, 4].map((bar) => (
        <span
          key={bar}
          className={
            bar <= bars
              ? "signal-bar active"
              : "signal-bar"
          }
          style={{
            height: `${8 + bar * 5}px`,
          }}
        />
      ))}
    </div>
  );
}

/* =========================================================
   STATUS BADGE
========================================================= */

function StatusBadge({ status }) {
  return (
    <span
      className={`status-badge ${status.toLowerCase()}`}
    >
      {status}
    </span>
  );
}

/* =========================================================
   CURRENT NETWORK STATUS
========================================================= */

function CurrentNetworkCard({ telemetry }) {
  const {
    rssi,
    speed,
    latency,
  } = telemetry;

  const critical = rssi < -80;

  const signalPercentage = clamp(
    ((rssi + 100) / 55) * 100,
    5,
    100
  );

  return (
    <section className="panel current-panel">

      {/* HEADER */}

      <div className="panel-heading">
        <h2>Current Network Status</h2>
      </div>

      {/* CURRENT LOCATION */}

      <div className="telemetry-row">

        <div className="row-label">
          <span className="tiny-marker pink" />
          CURRENT LOCATION
        </div>

        <div className="row-value">
          Main Tech Block
        </div>

        <div className="row-subvalue">
          Auto-detected GPS
        </div>

      </div>

      {/* CONNECTED NETWORK */}

      <div className="telemetry-row">

        <div className="row-label">
          <span className="tiny-marker blue" />
          CONNECTED
        </div>

        <div className="row-value mono">
          Student_HighSpeed_TechBlock
        </div>

      </div>

      {/* CURRENT SIGNAL */}

      <div className="telemetry-row signal-row">

        <div className="row-label">
          <span className="tiny-marker blue" />
          CURRENT SIGNAL
        </div>

        <div className="signal-main">

          <span
            className={
              critical
                ? "critical-value"
                : "healthy-value"
            }
          >
            {rssi} dBm
          </span>

          {critical && (
            <span className="critical-badge">
              <span>▲</span>
              Critical Dead Zone
            </span>
          )}

        </div>

        <div className="signal-track">

          <div
            className={
              critical
                ? "signal-fill critical"
                : "signal-fill healthy"
            }
            style={{
              width: `${signalPercentage}%`,
            }}
          />

        </div>

      </div>

      {/* CURRENT SPEED */}

      <div className="telemetry-row speed-row">

        <div className="row-label">
          <span className="tiny-marker orange" />
          CURRENT SPEED
        </div>

        <div
          className={
            speed < 10
              ? "speed-value critical-speed"
              : "speed-value"
          }
        >
          {speed.toFixed(1)} Mbps
        </div>

        <div className="speed-meta">

          <span>
            ↓{" "}
            {Math.max(
              0.1,
              speed * 0.9
            ).toFixed(1)}
          </span>

          <span>
            ↑{" "}
            {(speed * 0.1).toFixed(1)}
          </span>

          <span>
            Latency {latency}ms
          </span>

        </div>

      </div>

    </section>
  );
}

/* =========================================================
   BEST SPOT
========================================================= */

function BestSpotCard() {
  const best = BASE_NETWORKS[0];

  function openDirection() {
    /*
      Google Maps will be connected here later.

      For now we intentionally do NOT send the user
      away from WiSense.
    */

    console.log(
      "Google Maps direction:",
      best.direction
    );
  }

  return (
    <section className="panel best-panel">

      {/* HEADER */}

      <div className="panel-heading">

        <div className="green-heading">

          <span className="bulb">
            💡
          </span>

          <h2>
            Next Best Spot Indicator
          </h2>

        </div>

      </div>

      {/* BEST SPOT */}

      <div className="best-spot-block">

        <div className="row-label">

          <span className="tiny-marker purple" />

          BEST SPOT

        </div>

        <div className="best-name">
          Central Library Courtyard
        </div>

        <div className="best-network">

          {best.name}

          <span> · </span>

          {best.rssi} dBm

          <span> · </span>

          {best.speed} Mbps

        </div>

      </div>

      {/* DISTANCE */}

      <div className="distance-block">

        <div className="distance-label">

          <span>♟</span>

          DISTANCE TO GO

        </div>

        <div className="distance-value">

          {best.distance}

          <span>
            M
          </span>

        </div>

      </div>

      {/* DIRECTION */}

      <div className="direction-block">

        <div className="row-label">

          <span className="tiny-marker orange" />

          DIRECTION PATH

        </div>

        <button
          className="direction-button"
          type="button"
          onClick={openDirection}
        >
          Walk North-East ↗
        </button>

      </div>

      {/* STATS */}

      <div className="best-stats">

        <div className="mini-stat">

          <span>
            ETA
          </span>

          <strong>
            ~18s
          </strong>

        </div>

        <div className="mini-stat">

          <span>
            GAIN
          </span>

          <strong>
            +85 Mbps
          </strong>

        </div>

        <div className="mini-stat">

          <span>
            ACCURACY
          </span>

          <strong>
            94%
          </strong>

        </div>

      </div>

    </section>
  );
}

/* =========================================================
   TASK SELECTOR
========================================================= */

function TaskSelector({
  selectedTask,
  setSelectedTask,
}) {
  return (
    <div className="task-selector-wrap">

      <div className="task-selector-label">
        SELECT YOUR TASK
      </div>

      <div className="task-select-shell">

        <select
          className="task-select"
          value={selectedTask.id}
          onChange={(event) => {

            const task =
              TASKS.find(
                (item) =>
                  item.id ===
                  event.target.value
              );

            if (task) {
              setSelectedTask(task);
            }

          }}
        >

          {TASKS.map((task) => (
            <option
              key={task.id}
              value={task.id}
            >
              {task.label}
            </option>
          ))}

        </select>

        <span className="select-arrow">
          ↓
        </span>

      </div>

    </div>
  );
}

/* =========================================================
   NEARBY ROUTERS
========================================================= */

function NearbyRouters({
  networks,
  selectedTask,
}) {
  return (
    <section className="panel routers-panel">

      <div className="panel-heading routers-heading">

        <div>
          <div className="eyebrow">
            WIFI NODE SCAN
          </div>

          <h2>
            Nearby Available Routers
          </h2>
        </div>

      </div>

      <div className="router-list">

        {networks.map((network) => (

          <div
            className="router-row"
            key={network.name}
          >

            <div className="router-left">

              <SignalBars
                rssi={network.rssi}
              />

              <div>

                <div className="router-name">
                  {network.name}
                </div>

                <div className="router-rssi">
                  {network.rssi} dBm
                </div>

              </div>

            </div>

            <div className="router-right">

              <strong>
                {network.speed.toFixed(1)}
                {" "}
                Mbps
              </strong>

              <StatusBadge
                status={network.status}
              />

            </div>

          </div>

        ))}

      </div>

      {/* RECOMMENDATION */}

      <div className="recommendation-strip">

        <span className="recommendation-dot" />

        <strong>
          LibraryWing_5G
        </strong>

        <span>
          recommended for{" "}
          {selectedTask.label.toLowerCase()}
        </span>

      </div>

    </section>
  );
}

/* =========================================================
   VIDEO QUALITY PLOT
========================================================= */

function VideoQualityPlot({ speed }) {

  const qualityLevel =
    getVideoLevel(speed);

  /*
    Each point represents an estimated
    connection condition at that distance.
  */

  const points = [
    {
      distance: 4,
      level: 4,
    },
    {
      distance: 7,
      level: 4,
    },
    {
      distance: 10,
      level: 3,
    },
    {
      distance: 14.5,
      level: qualityLevel,
    },
    {
      distance: 18,
      level: Math.max(
        2,
        qualityLevel - 1
      ),
    },
    {
      distance: 22,
      level: 2,
    },
    {
      distance: 27,
      level: 1,
    },
  ];

  function xPosition(distance) {
    return (distance / 30) * 100;
  }

  function yPosition(level) {

    const positions = {
      4: 12,
      3: 36,
      2: 61,
      1: 85,
    };

    return positions[level];
  }

  return (
    <section className="panel analysis-panel">

      <div className="analysis-heading">

        <div>

          <div className="eyebrow">
            CONNECTIVITY ANALYSIS
          </div>

          <h2>
            Video Quality vs Distance
          </h2>

        </div>

        <div className="analysis-tag">
          LIVE
        </div>

      </div>

      <p className="analysis-description">
        Expected streaming quality as distance
        from the router increases.
      </p>

      <div className="scatter-wrapper">

        <div className="scatter-chart">

          {/* Y labels */}

          <div className="quality-label q4">
            4K UHD
          </div>

          <div className="quality-label q3">
            1080p
          </div>

          <div className="quality-label q2">
            720p
          </div>

          <div className="quality-label q1">
            480p
          </div>

          {/* GRID */}

          <div className="grid-line horizontal h1" />
          <div className="grid-line horizontal h2" />
          <div className="grid-line horizontal h3" />
          <div className="grid-line horizontal h4" />

          {/* DATA POINTS */}

          {points.map(
            (point, index) => (

              <div
                key={index}
                className="scatter-point"
                style={{
                  left: `${xPosition(
                    point.distance
                  )}%`,
                  top: `${yPosition(
                    point.level
                  )}%`,
                }}
              >
                <span />
              </div>

            )
          )}

          {/* CURRENT POSITION */}

          <div
            className="current-distance-line"
            style={{
              left: `${xPosition(
                14.5
              )}%`,
            }}
          >
            <span>
              14.5m
            </span>
          </div>

        </div>

        {/* X AXIS */}

        <div className="x-axis">

          <span>0m</span>
          <span>5m</span>
          <span>10m</span>
          <span>15m</span>
          <span>20m</span>
          <span>25m</span>
          <span>30m</span>

        </div>

        <div className="x-axis-title">
          DISTANCE FROM ROUTER
        </div>

      </div>

      {/* RESULT */}

      <div className="plot-insight">

        <span className="insight-dot" />

        <strong>
          {getVideoQuality(speed)}
        </strong>

        <span>
          estimated maximum quality at{" "}
          {speed.toFixed(1)} Mbps
        </span>

      </div>

    </section>
  );
}

/* =========================================================
   DOWNLOAD TIME PLOT
========================================================= */

function DownloadTimePlot({
  speed,
}) {

  const fileSize = 2;

  /*
    Data changes according to current speed.
  */

  const points = [
    {
      distance: 4,
      speed: 87,
    },
    {
      distance: 7,
      speed: 80,
    },
    {
      distance: 10,
      speed: 67,
    },
    {
      distance: 14.5,
      speed,
    },
    {
      distance: 18,
      speed: Math.max(
        12,
        speed * 0.65
      ),
    },
    {
      distance: 22,
      speed: Math.max(
        8,
        speed * 0.48
      ),
    },
    {
      distance: 27,
      speed: Math.max(
        4,
        speed * 0.3
      ),
    },
  ];

  const maxTime = 3600;

  function xPosition(distance) {
    return (distance / 30) * 100;
  }

  function yPosition(pointSpeed) {

    const seconds =
      calculateDownloadTime(
        fileSize,
        pointSpeed
      );

    return clamp(
      (seconds / maxTime) * 100,
      5,
      94
    );
  }

  const currentDownloadTime =
    calculateDownloadTime(
      fileSize,
      speed
    );

  return (
    <section className="panel analysis-panel">

      <div className="analysis-heading">

        <div>

          <div className="eyebrow">
            DOWNLOAD ANALYSIS
          </div>

          <h2>
            Download Time vs Distance
          </h2>

        </div>

        <div className="analysis-tag">
          2 GB FILE
        </div>

      </div>

      <p className="analysis-description">
        Estimated time required to download a
        2 GB file as distance from the router
        increases.
      </p>

      <div className="scatter-wrapper">

        <div className="scatter-chart download-chart">

          {/* Y labels */}

          <div className="quality-label q4">
            FAST
          </div>

          <div className="quality-label q3">
            ~1 MIN
          </div>

          <div className="quality-label q2">
            ~5 MIN
          </div>

          <div className="quality-label q1">
            SLOW
          </div>

          {/* GRID */}

          <div className="grid-line horizontal h1" />
          <div className="grid-line horizontal h2" />
          <div className="grid-line horizontal h3" />
          <div className="grid-line horizontal h4" />

          {/* DATA POINTS */}

          {points.map(
            (point, index) => (

              <div
                key={index}
                className="scatter-point download-point"
                style={{
                  left: `${xPosition(
                    point.distance
                  )}%`,
                  top: `${yPosition(
                    point.speed
                  )}%`,
                }}
              >
                <span />
              </div>

            )
          )}

          {/* CURRENT RESULT */}

          <div
            className="current-download-point"
            style={{
              left: `${xPosition(
                14.5
              )}%`,
              top: `${yPosition(
                speed
              )}%`,
            }}
          >
            <span>
              {formatTime(
                currentDownloadTime
              )}
            </span>
          </div>

        </div>

        {/* X AXIS */}

        <div className="x-axis">

          <span>0m</span>
          <span>5m</span>
          <span>10m</span>
          <span>15m</span>
          <span>20m</span>
          <span>25m</span>
          <span>30m</span>

        </div>

        <div className="x-axis-title">
          DISTANCE FROM ROUTER
        </div>

      </div>

      {/* RESULT */}

      <div className="plot-insight">

        <span className="insight-dot blue-dot" />

        <strong>
          2 GB DOWNLOAD
        </strong>

        <span>
          current estimated time:{" "}
          {formatTime(
            currentDownloadTime
          )}
        </span>

      </div>

    </section>
  );
}

/* =========================================================
   MAIN APP
========================================================= */

function App() {

  const [
    selectedTask,
    setSelectedTask,
  ] = useState(
    TASKS[0]
  );

  const [
    telemetry,
    setTelemetry,
  ] = useState(
    INITIAL_TELEMETRY
  );

  const [
    lastRefresh,
    setLastRefresh,
  ] = useState(
    new Date()
  );

  /*
    LIVE DEMO TELEMETRY

    Every 3 seconds the connection changes.

    This is intentionally a simulation for now.
    Later this will be replaced with real Wi-Fi
    observations from the WiSense backend.
  */

  useEffect(() => {

    const timer =
      setInterval(() => {

        setTelemetry(
          (current) => {

            /*
              Random movement.

              Positive movement:
              stronger connection.

              Negative movement:
              weaker connection.
            */

            const movement =
              Math.random() > 0.5
                ? 1
                : -1;

            const newRssi =
              clamp(
                current.rssi +
                  movement *
                    (1 +
                      Math.random() *
                        2),
                -92,
                -48
              );

            /*
              Convert RSSI to signal
              strength between 0 and 1.
            */

            const signalStrength =
              (newRssi + 100) / 52;

            /*
              Speed responds to signal.
            */

            const newSpeed =
              clamp(
                2 +
                  signalStrength *
                    85 +
                  (Math.random() -
                    0.5) *
                    5,
                2,
                92
              );

            /*
              Better signal = lower latency.
            */

            const newLatency =
              Math.round(
                clamp(
                  320 -
                    signalStrength *
                      250,
                  35,
                  320
                )
              );

            return {
              rssi:
                Math.round(
                  newRssi
                ),

              speed:
                newSpeed,

              latency:
                newLatency,
            };
          }
        );

      }, 3000);

    return () =>
      clearInterval(timer);

  }, []);

  /* =====================================================
     MANUAL REFRESH
  ===================================================== */

  function refreshTelemetry() {

    setTelemetry(
      (current) => {

        const newRssi =
          clamp(
            current.rssi +
              (Math.random() -
                0.25) *
                12,
            -92,
            -48
          );

        const signalStrength =
          (newRssi + 100) / 52;

        return {
          rssi:
            Math.round(
              newRssi
            ),

          speed:
            clamp(
              2 +
                signalStrength *
                  85,
              2,
              92
            ),

          latency:
            Math.round(
              clamp(
                320 -
                  signalStrength *
                    250,
                35,
                320
              )
            ),
        };
      }
    );

    setLastRefresh(
      new Date()
    );
  }

  /* =====================================================
     RANK NETWORKS
  ===================================================== */

  const rankedNetworks =
    useMemo(() => {

      return BASE_NETWORKS
        .map(
          (
            network,
            index
          ) => {

            /*
              The first network is connected
              to the live telemetry.
            */

            if (index !== 0) {
              return network;
            }

            return {
              ...network,

              rssi:
                telemetry.rssi,

              speed:
                telemetry.speed,

              status:
                getStatusFromSpeed(
                  telemetry.speed
                ),
            };
          }
        )
        .sort(
          (a, b) =>
            b.speed -
            a.speed
        );

    }, [telemetry]);

  return (
    <main className="app-shell">

      <div className="page-container">

        {/* =================================================
            HEADER
        ================================================= */}

        <header className="top-header">

          <div className="brand-block">

            <div className="ascii-line">
              =================================
            </div>

            <h1>
              WISENSE
            </h1>

            <div className="subtitle">
              INTELLIGENT WIFI ANALYSIS SYSTEM
            </div>

            <div className="ascii-line">
              =================================
            </div>

          </div>

          <div className="header-actions">

            <button
              className="refresh-button"
              onClick={
                refreshTelemetry
              }
              type="button"
            >
              ↻ REFRESH
            </button>

            <div className="monitoring">

              <span className="monitor-dot" />

              MONITORING

            </div>

          </div>

        </header>

        {/* LAST REFRESH */}

        <div className="refresh-info">

          LAST SCAN{" "}

          {lastRefresh.toLocaleTimeString(
            [],
            {
              hour: "2-digit",
              minute: "2-digit",
              second: "2-digit",
            }
          )}

        </div>

        {/* =================================================
            TASK SELECTOR
        ================================================= */}

        <TaskSelector
          selectedTask={
            selectedTask
          }
          setSelectedTask={
            setSelectedTask
          }
        />

        {/* =================================================
            TOP DASHBOARD
        ================================================= */}

        <div className="dashboard-grid">

          <CurrentNetworkCard
            telemetry={
              telemetry
            }
          />

          <BestSpotCard />

        </div>

        {/* =================================================
            NEARBY ROUTERS
        ================================================= */}

        <NearbyRouters
          networks={
            rankedNetworks
          }
          selectedTask={
            selectedTask
          }
        />

        {/* =================================================
            VIDEO QUALITY ANALYSIS
        ================================================= */}

        <VideoQualityPlot
          speed={
            telemetry.speed
          }
        />

        {/* =================================================
            DOWNLOAD TIME ANALYSIS
        ================================================= */}

        <DownloadTimePlot
          speed={
            telemetry.speed
          }
        />

        {/* =================================================
            FOOTER
        ================================================= */}

        <footer className="footer">

          <span>
            WISENSE v1.0.0
          </span>

          <span>
            © 2026 WIFI INTELLIGENCE SYSTEMS
          </span>

          <div className="footer-right">

            <span>
              SCAN RATE: 3s
            </span>

            <span>
              MODE: PASSIVE
            </span>

            <span>
              GPS: ACTIVE
            </span>

          </div>

        </footer>

      </div>

      {/* HELP */}

      <button
        className="help-button"
        type="button"
      >
        ?
      </button>

    </main>
  );
}

export default App;