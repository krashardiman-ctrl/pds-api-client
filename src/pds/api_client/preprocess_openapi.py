import yaml
import argparse
import tempfile
import subprocess


def preprocess(input: dict):

    new_tags_dict = {t['name']: t['name'][3:] for t in input['tags']}
    for path  in input['paths'].keys():
        tags = input['paths'][path]['get']['tags']
        new_tags = [new_tags_dict.get(tag, tag) for tag in tags]
        input['paths'][path]['get']['tags'] = new_tags

    return input


def main():

    parser = argparse.ArgumentParser(
                    prog='Process yaml openapi',
                    description='Remove features unsupported by openapi-generator, python-nextgen language',
    )
    parser.add_argument('input_yaml')

    args = parser.parse_args()

    with open(args.input_yaml, "r") as stream:
        try:
            input = yaml.safe_load(stream)
            preprocess(input)

        except yaml.YAMLError as exc:
            print(exc)

    with tempfile.NamedTemporaryFile(mode='w', delete=True) as file:
        yaml.dump(input, file)
        clean_cmd = ['rm', '-fr', 'pds', 'test']
        subprocess.run(clean_cmd)

        openapi_generator_cmd = [
            'openapi-generator',
            'generate',
            '-g',
            'python-nextgen',
            '-i',
            file.name,
            '--package-name',
            'pds.api_client',
            '--additional-properties=packageVersion={version}'
        ]
        subprocess.run(openapi_generator_cmd)

        replace_gitignore_cmd = ['cp', '.gitignore-orig',  '.gitignore']
        subprocess.run(replace_gitignore_cmd)


if __name__ == '__main__':
    main()