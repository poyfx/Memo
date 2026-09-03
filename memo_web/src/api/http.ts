const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ?? "http://127.0.0.1:8000";

type JsonRecord = Record<string, unknown>;

export async function requestJson<T>(
  path: string,
  init: RequestInit = {},
): Promise<T> {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...(init.headers ?? {}),
    },
    ...init,
  });

  const isJson = response.headers.get("content-type")?.includes("application/json");
  const payload = isJson ? ((await response.json()) as JsonRecord) : null;

  if (!response.ok) {
    const message =
      (payload && typeof payload.detail === "string" && payload.detail) ||
      (payload && typeof payload.message === "string" && payload.message) ||
      `Request failed: ${response.status}`;
    throw new Error(message);
  }

  return payload as T;
}
