{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "036e54a3-a735-4a11-857c-f579b0a9ec56",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "from langchain_groq import ChatGroq\n",
    "\n",
    "def get_groq_llm():\n",
    "    load_dotenv()\n",
    "    api_key = os.getenv(\"GROQ_API_KEY\")\n",
    "    if not api_key:\n",
    "        raise ValueError(\"GROQ_API_KEY not found in environment variables\")\n",
    "\n",
    "    llm = ChatGroq(\n",
    "        model=\"llama-3.1-8b-instant\",\n",
    "        api_key=api_key\n",
    "    )\n",
    "    return llm\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0df21cd-b97f-430a-a947-8aff60756c72",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
