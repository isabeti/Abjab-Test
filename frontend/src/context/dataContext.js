import React, { createContext, useContext, useState, useEffect } from "react";
import axios from "axios";

const DataContext = createContext();

export const useData = () => useContext(DataContext);

export const DataProvider = ({ children }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const [selectedLang, setSelectedLang] = useState("ir");
  const [enteredWord, setEnteredWord] = useState("");
  const [wordError, setwordError] = useState("");
  const [showWordBoxes, setShowWordBoxes] = useState(false);
  const [serchEntered, setSerchEntered] = useState("ir");

  const [boxesData, setBoxesData] = useState(null);

  console.log(showWordBoxes);

  const handleSelectLang = (lang) => {
    setSelectedLang(lang);
    serchEntered === lang && localStorage.setItem("selectedLang", lang);
  };

  let boxes;

  const formData = new URLSearchParams();
  formData.append("word", enteredWord.toString());

  const handleSearchFa = async () => {
    try {
      const response = await axios.post(
        "http://iiisabeti.pythonanywhere.com/abjad-calculate-fa/",
        formData,
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );

      if (!response.data) {
        throw new Error("Empty response received");
      }

      console.log("Response from server:", response.data.data.box);

      localStorage.setItem("selectedLang", selectedLang);
      setBoxesData(response.data.data.box);
    } catch (error) {
      console.error("There was a problem with your axios operation:", error);
    }
  };

  const handleSearchEn = async () => {
    try {
      const response = await axios.post(
        "http://iiisabeti.pythonanywhere.com/abjad-calculate-en/",
        formData,
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );

      if (!response.data) {
        throw new Error("Empty response received");
      }

      console.log("Response from server:", response.data.data.box);

      localStorage.setItem("selectedLang", selectedLang);
      setBoxesData(response.data.data.box);
    } catch (error) {
      console.error("There was a problem with your axios operation:", error);
    }
  };

  console.log(boxes);
  console.log(boxesData);

  return (
    <DataContext.Provider
      value={{
        data,
        loading,
        handleSearchFa,
        boxesData,
        selectedLang,
        handleSelectLang,
        enteredWord,
        setEnteredWord,
        wordError,
        setwordError,
        showWordBoxes,
        setShowWordBoxes,
        handleSearchEn,
        serchEntered,
        setSerchEntered,
      }}
    >
      {children}
    </DataContext.Provider>
  );
};
