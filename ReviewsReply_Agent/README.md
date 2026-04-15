# AI Review Reply Agent 🤖🍽️

An intelligent, local LLM-powered system designed to automate and professionalize the process of responding to restaurant reviews. By leveraging state-of-the-art AI, this agent ensures that every customer feels heard while maintaining a consistent and premium brand voice.

## Overview

In the fast-paced hospitality industry, responding to every Google or Yelp review is time-consuming but critical for SEO and customer retention. The AI Review Reply Agent simplifies this by:

* Automatically extracting review narratives from messy metadata.
* Generating sentiment-aware, professional responses.
* Organizing reviews into dedicated monthly registries (DOCX format) for easy business auditing.

## Key Features

* AI-generated review responses powered by Ollama (Mistral 7B) for human-like, contextually relevant replies.
* Sentiment-aware replies that detect the tone of the customer (1-star to 5-star) and adjust the response strategy accordingly.
* Multiple response styles including short/concise and detailed/premium responses depending on the review depth.
* Custom brand tone support tailored for restaurant groups like Aroma Indian Cuisine and Urban Indian, ensuring unique sign-offs and brand identity.
* Ready-to-use reply templates (text tags) using standardized placeholders such as [Customer Name] to maintain high consistency across interactions.
* Document vault that automatically archives every review and reply into structured monthly Word documents for long-term record keeping.

## Tech Stack

* Frontend: Responsive dashboard built with HTML5, Vanilla JavaScript, and Tailwind CSS.
* Backend: Python (Flask) for routing and logic.
* AI Integration: Ollama (Mistral 7B) running locally for maximum data privacy and cost efficiency.
* Document Processing: python-docx for automated report generation.

## How It Works

1. Input: Copy-paste a raw Google review into the dashboard.
2. Narrative extraction: The system cleans the input, removing metadata like "Dine in," "Price," and review counts.
3. Prompt engineering: A structured prompt is sent to the local LLM, incorporating the reviewer’s name and the specific restaurant’s brand rules.
4. Generation: The AI generates a two-paragraph response where the customer’s name is naturally integrated.
5. Storage: The cleaned review and the AI reply are saved to the Document Vault in a .docx file for the current month.

## Sample Input & Output

Input Review:
"John Doe
5 reviews · 2 photos
The food was spicy and delicious! Service was a bit slow but the atmosphere made up for it. Price: ₹1,000–2,000"

Generated Output:
"The vibrant flavors and spice levels were truly enjoyed by John Doe. We are thrilled you appreciated the atmosphere and found our culinary offerings to your liking.

We appreciate your feedback regarding the service speed and are committed to refining our efficiency. We look forward to welcoming you back for an even smoother experience.

Team Urban Indian."

## Use Cases

* Restaurants: Scale guest relations across multiple locations.
* Retail businesses: Quickly address Google My Business feedback.
* Customer support teams: Streamline response drafting for high-volume review sites.

## Setup Instructions

1. Install Ollama: Download from https://ollama.com
2. Pull Model:
   ollama pull mistral
