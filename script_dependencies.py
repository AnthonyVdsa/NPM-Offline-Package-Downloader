import json
import subprocess

already_dl = set()

def get_dependencies(package_lock_file_path):
    subprocess.run(["npm", "i", "--package-lock-only", "--legacy-peer-deps"])
    subprocess.run(["mkdir", "npm_packages_downloaded"])
    with open(package_lock_file_path, 'r') as file:
        package_lock_file = json.load(file)
        if 'packages' in package_lock_file:
            for package_name, package_infos in package_lock_file['packages'].items():
                if package_name != '' and package_name not in already_dl:
                    try:
                        version = package_infos.get('version')
                        pkg_name = package_name.split('node_modules/')[len(package_name.split('node_modules/')) - 1] + "@" + version
                        subprocess.run(["npm", "pack", pkg_name, "--pack-destination", "npm_packages_downloaded"])
                        already_dl.add(package_name)
                    except Exception as e:
                        print(e)
                        print(f'The installation of {package_name} failed')

    subprocess.run(["tar", "czf", "npm_packages_downloaded.tar", "npm_packages_downloaded"])
    subprocess.run(["mv", "npm_packages_downloaded.tar", "/npm_packages_downloaded"])

package_lock_file_path = './package-lock.json'
get_dependencies(package_lock_file_path)
