"use server";
import { NextResponse } from "next/server";

export async function translate(sentence: string): Promise<string> {
  try {
    const res = await fetch(`${process.env.BASE_URL!}/api/translate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sentence }),
    });

    if (!res.ok) {
      throw new Error(`Translation request failed with status: ${res.status}`);
    }

    const data = await res.json();

    return data.translation || "";
  } catch (error) {
    console.error("Translation error:", error);
    return "Translation error occurred. Please try again later.";
  }
}
