import kconfig
import parse_rest.connection

def get_keys():
	config_path = kconfig.ConfigPathDefaults([".psrd", "~/.psrd", "/etc/psrd"])
	kconfig.Config().config_path = config_path
	return kconfig.Config().fetch_config("parse")

def register():
	config = get_keys()
	parse_rest.connection.register(
		config["application_id"],
		config["rest_api_key"],
		master_key=config["master_key"])
