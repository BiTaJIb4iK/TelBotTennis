 
# class SelectedCourtMiddleware(BaseMiddleware):
#     def __init__(self) -> None:
#         self.selected_court = -1
#         self.selected_day = -1
#         self.selected_time = -1

#     async def __call__(
#         self,
#         handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
#         event: CallbackQuery,
#         data: Dict[str, Any]
#     ) -> Any:
#         data['selected_court'] = self.selected_court
#         data['selected_day'] = self.selected_day
#         data['selected_time'] = self.selected_time
#         return await handler(event, data)