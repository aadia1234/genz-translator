"use client";

export async function translate(sentence: string): Promise<string> {
  try {
    // comment
    const apiUrl = "/api/translate";
    const res = await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "text/plain",
        "Accept": "text/plain, */*",
        "Cache-Control": "no-cache",
      },
      body: sentence,
      cache: "no-store",
    });

    console.log("URL: " + apiUrl);

    if (!res.ok) {
      throw new Error(`Translation request failed with status: ${res.status}`);
    }

    const data = await res.text();

    return data || "";
  } catch (error) {
    console.error("Translation error:", error);
    return "Translation error occurred. Please try again later.";
  }
}
