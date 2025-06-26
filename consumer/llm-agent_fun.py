# from lyzr_automata.ai_models.openai import OpenAIModel
# from lyzr_automata.ai_models.perplexity import PerplexityModel
# from lyzr_automata import Agent
# from lyzr_automata.tasks.task_literals import InputType, OutputType
# from lyzr_automata import Task
# from lyzr_automata.tools.prebuilt_tools import linkedin_image_text_post_tool
# from lyzr_automata.tasks.util_tasks import summarize_task
# from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
# import os

# # We will first create open ai model for our language tasks

# open_ai_model_text = OpenAIModel(
#     api_key=  os.getenv("OPENAI_API_KEY"),
#     parameters={
#         "model": "gpt-4-turbo-preview",
#         "temperature": 0.2,
#         "max_tokens": 1500,
#     },
# )

# # open_ai_model_image = OpenAIModel(
# #     api_key=os.getenv('OPEN_AI_KEY'),
# #     parameters={
# #         "n": 1,
# #         "model": "dall-e-3",
# #     },
# # )


# perplexity_model_text = PerplexityModel(
#     api_key=os.getenv('PP_AI_KEY'),
#     parameters={
#         "model": "pplx-70b-online",
#     },
# )



# # Content researcher agent for our search task
# content_researcher_agent = Agent(
#     prompt_persona="You are an AI journalist good at using the provided data to conduct research and present understandanble points",
#     role="AI Journalist",
# )

# # Linkedin content creator agent for your linkedin content writing task
# # linkedin_content_writer_agent = Agent(
# #     prompt_persona="You write engaging linkedin posts with the provided input data",
# #     role="Linkedin Content Creator",
# # )


# # You can access our prebuilt tools
# # or you can use our base tools class to create your own tool
# linkedin_post_tool = linkedin_image_text_post_tool(
#     owner=os.getenv('LK-OWNER'),
#     token=os.getenv('LK-TOKEN'),
# )
# search_task = Task(
#     name="Search Latest information of all stocks in incoming streams",
#     output_type=OutputType.TEXT,
#     input_type=InputType.TEXT,
#     model=perplexity_model_text,
#     instructions="Search,collect and evaluate  all latest news about the Stock",
#     log_output=True,
# )

# research_task = Task(
#     name="Draft Content Creator",
#     agent=content_researcher_agent,
#     output_type=OutputType.TEXT,
#     input_type=InputType.TEXT,
#     model=open_ai_model_text,
#     instructions="Analyze the input and clean the data and write a summary of 1000 words which can be used to create Linkedin post in the next task",
#     log_output=True,
#     enhance_prompt=False,
# )

# # linkedin_content_writing_task = Task(
# #     name="Linkedin Post Creator",
# #     agent=linkedin_content_writer_agent,
# #     output_type=OutputType.TEXT,
# #     input_type=InputType.TEXT,
# #     model=open_ai_model_text,
# #     instructions="Use the news summary provided and write 1 engaging linkedin post of 200 words",
# #     log_output=True,
# #     enhance_prompt=False,

# # )


# # image_creation_task = Task(
# #     name="Linkedin Image Creation",
# #     output_type=OutputType.IMAGE,
# #     input_type=InputType.TEXT,
# #     model=open_ai_model_image,
# #     log_output=True,
# #     instructions="Use the research material provided and create a linkedin post image that would be suitable for posting",
# # )


# linkedin_upload_task = Task(
#     name="Linkedin Post Task",
#     model=open_ai_model_text,
#     tool=linkedin_post_tool,
#     instructions="Post on Linkedin",
#     input_tasks=[linkedin_content_writing_task, image_creation_task],
# )


# # Use our LinearSyncPipeline to run tasks linearly in sync way
# # We are also using summarize_task from our prebuilt tasks because image creation dalle model has a shorter limit

# def main():
#     LinearSyncPipeline(
#         name="Automated Linkedin Post",
#         completion_message="Posted Successfully 🎉",
#         tasks=[
#             search_task,
#             research_task,
#             linkedin_content_writing_task,
#             image_creation_task,
#             linkedin_upload_task,
#         ],
#     ).run()


# main()