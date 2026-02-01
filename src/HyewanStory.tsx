import { AbsoluteFill, Img, interpolate, useCurrentFrame, useVideoConfig, staticFile, Sequence } from "remotion";

// 장면 데이터
const scenes = [
  {
    id: "001",
    image: "scene_001.jpeg",
    duration: 15,
    narration: "여름방학이 시작된 어느 날, 혜완이는 엄마 아빠와 함께 특별한 여행을 떠났어요.",
    kenBurns: { startScale: 1, endScale: 1.15, startX: 0, endX: -30 }
  },
  {
    id: "002",
    image: "scene_002.png",
    duration: 18,
    narration: "대전에서 밀양까지, 빠른 기차를 타고 가는 길. 창밖으로 논과 산이 빠르게 지나갔어요.",
    kenBurns: { startScale: 1.1, endScale: 1, startX: 20, endX: 0 }
  },
  {
    id: "003",
    image: "scene_003.jpeg",
    duration: 15,
    narration: "밀양역에 도착하니, 할머니 할아버지가 환하게 웃으며 기다리고 계셨어요.",
    kenBurns: { startScale: 1, endScale: 1.2, startX: 0, endX: 0 }
  },
  {
    id: "004",
    image: "scene_004.png",
    duration: 12,
    narration: "\"할머니!\" 혜완이는 할머니 품에 폭 안겼어요.",
    kenBurns: { startScale: 1.2, endScale: 1.3, startX: 0, endX: 0 }
  }
];

// 단일 장면 컴포넌트
const Scene: React.FC<{
  image: string;
  narration: string;
  kenBurns: { startScale: number; endScale: number; startX: number; endX: number };
  durationInFrames: number;
}> = ({ image, narration, kenBurns, durationInFrames }) => {
  const frame = useCurrentFrame();

  const scale = interpolate(
    frame,
    [0, durationInFrames],
    [kenBurns.startScale, kenBurns.endScale],
    { extrapolateRight: "clamp" }
  );

  const translateX = interpolate(
    frame,
    [0, durationInFrames],
    [kenBurns.startX, kenBurns.endX],
    { extrapolateRight: "clamp" }
  );

  const textOpacity = interpolate(
    frame,
    [0, 15, durationInFrames - 15, durationInFrames],
    [0, 1, 1, 0],
    { extrapolateRight: "clamp" }
  );

  return (
    <AbsoluteFill style={{ backgroundColor: "black" }}>
      {/* 이미지 with Ken Burns */}
      <div
        style={{
          width: "100%",
          height: "100%",
          overflow: "hidden",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Img
          src={staticFile(`scenes/${image}`)}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "cover",
            transform: `scale(${scale}) translateX(${translateX}px)`,
          }}
        />
      </div>

      {/* 나레이션 자막 */}
      <div
        style={{
          position: "absolute",
          bottom: 80,
          left: 0,
          right: 0,
          display: "flex",
          justifyContent: "center",
          opacity: textOpacity,
        }}
      >
        <div
          style={{
            backgroundColor: "rgba(0, 0, 0, 0.7)",
            padding: "20px 40px",
            borderRadius: 10,
            maxWidth: "80%",
          }}
        >
          <p
            style={{
              color: "white",
              fontSize: 36,
              fontFamily: "Noto Sans KR, sans-serif",
              textAlign: "center",
              margin: 0,
              lineHeight: 1.5,
            }}
          >
            {narration}
          </p>
        </div>
      </div>
    </AbsoluteFill>
  );
};

// 메인 스토리 컴포넌트
export const HyewanStory: React.FC = () => {
  const { fps } = useVideoConfig();

  let currentFrame = 0;

  return (
    <AbsoluteFill>
      {scenes.map((scene, index) => {
        const durationInFrames = scene.duration * fps;
        const startFrame = currentFrame;
        currentFrame += durationInFrames;

        return (
          <Sequence
            key={scene.id}
            from={startFrame}
            durationInFrames={durationInFrames}
          >
            <Scene
              image={scene.image}
              narration={scene.narration}
              kenBurns={scene.kenBurns}
              durationInFrames={durationInFrames}
            />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
