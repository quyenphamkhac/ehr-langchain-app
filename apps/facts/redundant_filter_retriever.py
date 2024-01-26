from typing import Any, Coroutine, Dict, List, Optional
from langchain_community.vectorstores.chroma import Chroma
from langchain.schema import BaseRetriever
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings


class RedundantFilterRetriever(BaseRetriever):
    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query: str) -> List[Document]:
        # calculate embeddings for the 'query' string
        emb = self.embeddings.embed_query(query)

        # take embeddings and feed them into that
        # max_marginal_relevance_search_by_vector
        return self.chroma.max_marginal_relevance_search_by_vector(
            embedding=emb,
            lambda_mult=0.8
        )

    async def aget_relevant_documents(self) -> List[Document]:
        return []
