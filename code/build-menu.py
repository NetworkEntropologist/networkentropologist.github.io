
from datetime import datetime

import frontmatter
import os
import yaml

# Run this from the project root!
post_path = 'docs/_posts'

post_files_list = []
post_list = []

tag_cloud = {}

# Sample of each post entry in posts_list
post_sample_yaml = {
    'title': '',
    'date': '',
    'tags': [],
}


# Rough flow for this procedure:
# First get a list of posts
# Iterate the list of posts and load the metadata for each
# Build the top posts menu
# Build the archive menu
# Build the tag cloud
# Write the top menu
# Write the archive menu
# Write the tag cloud

def load_post_metadata(post_file):
    post = frontmatter.load(os.path.join(post_path, post_file))
    metadata = post.metadata
    return metadata

def build_tag_cloud():
    for post in post_list:
        for tag in post['tags']:
            print(f"Processing tag: {tag}")
            if tag not in tag_cloud:
                tag_cloud[tag] = 1
            else:
                tag_cloud[tag] += 1


post_files_list = os.listdir(post_path)

for post_file in post_files_list:
    metadata = load_post_metadata(post_file)
    post_list.append(metadata)
    # print(metadata['tags'])

build_tag_cloud()

# print(yaml.dump(post_list, indent=2))
print(yaml.dump(tag_cloud, indent=2))

