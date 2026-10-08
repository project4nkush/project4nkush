import os
import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader

def main():
    # 1. Set up Jinja2 template engine (load templates relative to this script)
    base_dir = os.path.dirname(__file__)
    templates_dir = os.path.join(base_dir, "templates")
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template("post.html")

    # 2. Load the source file
    src_path = os.path.join(base_dir, "content", "posts", "aec", "2026-09-24-dynamo-basics.md")
    post_data = frontmatter.load(src_path, encoding="utf-8-sig")

    # 3. Convert the markdown to HTML
    html_content = markdown.markdown(post_data.content)

    # 4. Assemble what the template needs
    # Copy metadata and inject the body HTML string
    post_dict = post_data.metadata.copy()
    post_dict["body"] = html_content

    # 4.5 Find the root path from the output file's location
    dest_path = os.path.join(base_dir, "blog", "aec", "2026-09-24-dynamo-basics.html")
    rel_output = os.path.relpath(dest_path, base_dir)
    depth = rel_output.count(os.sep)
    root_path = "../" * depth
    
    # 5. Render the template
    rendered_html = template.render(post=post_dict, root_path=root_path)

    # Create the folder if it's missing
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)

    # Save the rendered HTML file
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"Successfully generated: {dest_path}")

if __name__ == "__main__":
    main()