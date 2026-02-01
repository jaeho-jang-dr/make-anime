import { Composition } from "remotion";
import { HyewanStory } from "./HyewanStory";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="HyewanStory"
        component={HyewanStory}
        durationInFrames={30 * 70} // 70초 (4개 장면 테스트)
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
