"use client"

import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { translate } from "./actions"
import { useState } from "react";
import { LoaderCircle } from "lucide-react";

export default function Home() {
  const [sentence, setSentence] = useState("");
  const [translation, setTranslation] = useState("");
  const [loading, setLoading] = useState(false);

  const handleTranslate = async () => {
    setLoading(true);

    try {
      const result = await translate(sentence);
      setTranslation(result);
    } catch (error) {
      console.error("Error translating:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white grid grid-rows-[56px_1fr_56px] items-center justify-items-center min-h-screen font-[family-name:var(--font-geist-sans)]">
      <main className="w-[50%] gap-[32px] flex flex-col row-start-2 items-center text-gray-600">
        <p className="text-5xl">Shakespeare Translator</p>
        <div className="flex w-full max-w-2xl items-center space-x-2">
          <Input type="text" placeholder="Enter the sentence you'd like to translate" onChange={(event) => setSentence(event.target.value)} />
          <Button type="submit" onClick={handleTranslate}>Translate</Button>
        </div>
        {
          translation &&
          <div className="w-full max-w-2xl items-center text-center justify-center space-y-2">
            <p className="text-2xl">{loading ? "Translating..." : "Translated Sentence:"}</p>
            {
              loading ?
                <LoaderCircle className="mx-auto animate-spin text-gray-600" />
                :
                <p className="text-xl">{translation}</p>
            }
          </div>
        }
      </main>
      <footer className="bg-gray-200 w-full h-14 row-start-3 flex items-center justify-center">
        <a
          className="text-gray-600 flex items-center hover:underline hover:underline-offset-4"
          href="https://www.aadiananddeveloper05.com"
          target="_blank"
          rel="noopener noreferrer"
        >
          © 2025 Aadi Anand
        </a>
      </footer>
    </div>
  );
}
