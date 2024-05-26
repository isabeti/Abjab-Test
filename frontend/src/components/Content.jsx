import { useData } from "../context/dataContext";
import Slider from "../components/slider/Slider";
import WordBoxes from "../components/word-boxes/WordBoxes";
import WordTable from "../components/word-table/WordTable";

const Content = () => {
  const { showWordBoxes } = useData();

  return (
    <>
      {showWordBoxes ? (
        <>
          <WordBoxes />
          <WordTable />
        </>
      ) : (
        <Slider />
      )}
    </>
  );
};

export default Content;
