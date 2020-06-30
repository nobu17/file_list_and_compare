from domains.services.path_service import PathService
from infrastructure.os_path_repository import OSPathRepository
from infrastructure.os_path_factory import OSPathFactory
from domains.applications.path_app_service import PathAppService
from console.console_controller import ConsoleController
from console.console_args import ConsoleArgs
import sys
import traceback
sys.path.append('.console')


args = ConsoleArgs(sys.argv)

repository = OSPathRepository(OSPathFactory())
app_service = PathAppService(PathService(repository), repository)
controller = ConsoleController(app_service)

try:
    controller.exec(args)
    print("execution is finished.")
    sys.exit(0)
except Exception as e:
    print("Error:{}".format(e))
    print(traceback.format_exc())
    sys.exit(1)
