class AnySearchRetrieverClient:
    def restructure_data(self, raw_unstructured_data: str) -> dict:
        # Simple mock tag splitter
        pairs = [p.split(":") for p in raw_unstructured_data.split(",") if ":" in p]
        structured = {k.strip(): v.strip() for k, v in pairs}
        return {"structured_json": structured}