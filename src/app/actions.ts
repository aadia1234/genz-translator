"use server";

export async function translate(sentence: string): Promise<string> {
  try {
    // comment
    const res = await fetch(`${process.env.BASE_URL!}/api/translate`, {
      method: "POST",
      headers: { "Content-Type": "text/plain" },
      body: sentence,
    });

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
