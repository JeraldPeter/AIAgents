from dataclasses import dataclass

@dataclass
class ResearchConfiguration:
    """Configuration for research-related models and parameters.

    Attributes:
        critic_model (str): Model for evaluation tasks.
        worker_model (str): Model for working/generation tasks.
        max_search_iterations (int): Maximum search iterations allowed.
    """

    critic_model: str = "gemini-3-pro-preview"
    worker_model: str = "gemini-3-pro-preview"
    max_search_iterations: int = 5


config = ResearchConfiguration()
