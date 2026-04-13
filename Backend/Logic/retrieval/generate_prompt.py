
def generate_prompt(query, retrieved_docs):

    docs = retrieved_docs["documents"][0]
    metas = retrieved_docs["metadatas"][0]
    distances = retrieved_docs["distances"][0]

    context = "\n\n".join(
    f"[Document: {meta.get('document')}, "
    f"Section: {(meta.get('headings') or ['No Heading'])[0]}, "
    f"Page: {format_pages(meta.get('page'))}]: \n{doc}"
    for i, (doc, meta) in enumerate(zip(docs, metas))
)
    print(context)
    print(distances)

    prompt = f"""
        You are a helpful study assistant.
        
        INSTRUCTIONS: 
        1. Answer the question using the information provided in the context below.
        2. The context paragraphs are ordered by relevance (most relevant first). Prioritize information from higher ranked paragraphs.
        3. Ignore any in-text citations, references, or bibliographies that appear within the context itself.
        4. Reference every Information derived from the context using numbered in-text citation (e.g. [1]). 
        5. After the Answer, include a section starting with "Sources: ", listing all references in the Format: "[1] Document name,heading, page, [2] Document name,heading, page"
        6. If the answer cannot be found in the context, respond with: "I don't know based on the provided documents."
        
        EXAMPLE: "
        Question: What is Principal Component Analysis and how does it work?
        Context:
        [Document: PCA.pdf, Section: PCA, Page: 25-26]:
        passage: Principal Component Analysis (PCA) is a technique to reduce the dimensionality of a dataset by transforming correlated variables into a smaller set of uncorrelated principal components while preserving variance (Rebecca, 2018). The covariance matrix is computed and decomposed to find eigenvectors and eigenvalues.
        
        [Document: Eigenvectors.pdf, Section: PCA, Page 15]:
        passage: Eigenvectors define the directions of the principal components, and eigenvalues measure the variance along them (Keller et al., 2018). Typically, only the top k components are retained, and the data is projected onto these components.
        
        Answer:
        "Principal Component Analysis (PCA) reduces the dimensionality of data while preserving variance [1]. It centers the data, computes the covariance matrix, and finds eigenvectors and eigenvalues to define principal components [1]. The top components, ranked by variance, are used to project the data into a lower-dimensional space [2]."
        \n
        Sources:[1] (PCA.pdf, Section: PCA, Page: 25-26), [2] (PCA.pdf, Section: PCA, Page: 25-26), [3]: (Eigenvectors.pdf,  Section: PCA, Page: 15)"
        "

        CONTEXT:
        {context}

        QUESTION:
        {query}

        ANSWER:
        """
    
    print(prompt.strip())

    return prompt.strip()


def format_pages(pages):
    if not pages:
        return "Unknown Page"
    pages = sorted(set(pages))
    return str(pages[0]) if len(pages) == 1 else f"{pages[0]}-{pages[-1]}"



'''Extensive Example for Prompt with Additional Information allowed.'''
# [Document: 1, Section: PCA, Page: 25-26]:
# passage: Principal Component Analysis (PCA) is a linear dimensionality reduction technique that transforms a dataset with possibly many correlated variables into a smaller set of uncorrelated variables called principal components, while retaining as much of the original variance as possible. 
# The covariance matrix of the data is computed to capture how variables vary together. PCA proceeds by solving an eigenvalue decomposition of this covariance matrix, yielding eigenvectors and corresponding eigenvalues.

# [Document: 2, Section: PCA, Page 26]:
# passage: The eigenvectors represent directions in the feature space (principal components), and the eigenvalues quantify how much variance is captured along each direction.
# The components are ranked by their eigenvalues, and typically only the top k components are retained.
# Finally, the original data is projected onto these top k eigenvectors, producing a lower-dimensional representation. 

# Answer: 
# "Principal Component Analysis (PCA) is a statistical technique used to reduce the dimensionality of a dataset while preserving as much of its variability as possible.
# It works by first centering the data (subtracting the mean), then computing the covariance matrix to capture relationships between features [1].
# Next, it finds the eigenvectors and eigenvalues of this matrix: the eigenvectors define new orthogonal directions called principal components, and the eigenvalues indicate how much variance each component explains. 
# The components are sorted by their explained variance, and the data is projected onto the top few components, resulting in a lower-dimensional representation that retains most of the original information [2].
# \n
# Additional Info: PCA is widely used for data compression, noise reduction, visualization, and as a preprocessing step for machine learning models.
# \n
# Sources:[1] (Document: Document 1, Section: PCA, Page: 25-26), [2]: (Document: Document 2,  Section: PCA, Page: 26)"
# "