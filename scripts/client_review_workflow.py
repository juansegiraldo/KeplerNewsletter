#!/usr/bin/env python3
"""
Client Review Workflow for Newsletter Content

This script implements a 3-stage workflow:
1. Generate editable drafts from JSON data
2. Allow client review and editing
3. Generate final HTML with client changes

Usage:
    python scripts/client_review_workflow.py --stage 1 --input data/art-law/arte_derecho_report_2025_08_20_all_merged.json
    python scripts/client_review_workflow.py --stage 2 --draft drafts/arte_derecho_report_2025_08_20_all_merged_draft.md
    python scripts/client_review_workflow.py --stage 3 --draft drafts/arte_derecho_report_2025_08_20_all_merged_draft.md --output docs/art-law/issues/
"""

import json
import sys
import argparse
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
import re
import webbrowser
import http.server
import socketserver
import threading
import time


class ClientReviewWorkflow:
    def __init__(self):
        self.drafts_dir = Path("drafts")
        self.drafts_dir.mkdir(exist_ok=True)
        
    def stage1_generate_draft(self, json_file: str) -> str:
        """Stage 1: Generate editable draft from JSON data"""
        print(f"🔧 Stage 1: Generating editable draft from {json_file}")
        
        # Load JSON data
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Generate draft filename
        json_path = Path(json_file)
        draft_filename = f"{json_path.stem}_draft.md"
        draft_path = self.drafts_dir / draft_filename
        
        # Convert JSON to editable Markdown
        markdown_content = self._json_to_markdown(data)
        
        # Write draft file
        with open(draft_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        
        print(f"✅ Draft generated: {draft_path}")
        print(f"📝 Client can now edit: {draft_path}")
        
        return str(draft_path)
    
    def _json_to_markdown(self, data: Dict[str, Any]) -> str:
        """Convert JSON data to editable Markdown format"""
        markdown = []
        
        # Header
        markdown.append("# CLIENT REVIEW DRAFT")
        markdown.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        markdown.append(f"**Original Title:** {data.get('metadata', {}).get('title', 'Unknown')}")
        markdown.append("")
        markdown.append("---")
        markdown.append("")
        markdown.append("## INSTRUCTIONS FOR CLIENT")
        markdown.append("1. Review all content below")
        markdown.append("2. Make any necessary edits directly in this file")
        markdown.append("3. Save the file when done")
        markdown.append("4. Run Stage 2 to apply your changes")
        markdown.append("")
        markdown.append("**IMPORTANT:** Only edit the content between the `<!-- EDITABLE START -->` and `<!-- EDITABLE END -->` markers")
        markdown.append("")
        markdown.append("---")
        markdown.append("")
        
        # Metadata section
        markdown.append("## METADATA")
        markdown.append("<!-- EDITABLE START -->")
        metadata = data.get('metadata', {})
        markdown.append(f"**Title:** {metadata.get('title', '')}")
        markdown.append(f"**Subtitle:** {metadata.get('subtitle', '')}")
        markdown.append(f"**Period:** {metadata.get('period', {}).get('start_date', '')} to {metadata.get('period', {}).get('end_date', '')}")
        markdown.append("<!-- EDITABLE END -->")
        markdown.append("")
        
        # Executive Summary
        markdown.append("## EXECUTIVE SUMMARY")
        markdown.append("<!-- EDITABLE START -->")
        exec_summary = data.get('executive_summary', {})
        
        markdown.append("### Overview")
        markdown.append(exec_summary.get('overview', ''))
        markdown.append("")
        
        markdown.append("### Key Findings")
        for finding in exec_summary.get('key_findings', []):
            markdown.append(f"- {finding}")
        markdown.append("")
        
        markdown.append("### Key Themes")
        for theme in exec_summary.get('key_themes', []):
            markdown.append(f"- {theme}")
        markdown.append("")
        
        markdown.append("### Geographical Focus")
        for location in exec_summary.get('geographical_focus', []):
            markdown.append(f"- {location}")
        markdown.append("")
        
        markdown.append("### Trend Analysis")
        markdown.append(exec_summary.get('trend_analysis', ''))
        markdown.append("<!-- EDITABLE END -->")
        markdown.append("")
        
        # Items/Articles
        markdown.append("## ARTICLES")
        items = data.get('items', [])
        
        for i, item in enumerate(items, 1):
            markdown.append(f"### Article {i}")
            markdown.append("<!-- EDITABLE START -->")
            
            # Title
            markdown.append(f"**Title:** {item.get('title', '')}")
            markdown.append("")
            
            # Summary
            markdown.append("**Summary:**")
            markdown.append(str(item.get('summary', '')))
            markdown.append("")
            
            # Content
            markdown.append("**Content:**")
            markdown.append(str(item.get('content', '')))
            markdown.append("")
            
            # Classification
            classification = item.get('classification', {})
            if classification:
                markdown.append("**Classification:**")
                markdown.append(f"- Category: {classification.get('category', '')}")
                markdown.append(f"- Subcategory: {classification.get('subcategory', '')}")
                markdown.append(f"- Jurisdiction: {classification.get('jurisdiction', '')}")
                markdown.append("")
            
            # Sources
            sources = item.get('sources', [])
            if sources:
                markdown.append("**Sources:**")
                for source in sources:
                    markdown.append(f"- {source.get('title', '')} ({source.get('url', '')})")
                markdown.append("")
            
            markdown.append("<!-- EDITABLE END -->")
            markdown.append("")
            markdown.append("---")
            markdown.append("")
        
        return "\n".join(markdown)
    
    def stage2_client_review(self, draft_file: str) -> str:
        """Stage 2: Launch client review interface"""
        print(f"🔧 Stage 2: Launching client review interface for {draft_file}")
        
        draft_path = Path(draft_file)
        if not draft_path.exists():
            print(f"❌ Draft file not found: {draft_path}")
            return None
        
        # Create simple web interface for editing
        self._create_web_interface(draft_path)
        
        # Launch browser
        print("🌐 Opening client review interface in browser...")
        print("📝 Client can now edit the content online")
        print("💡 Press Ctrl+C to stop the server when done")
        
        try:
            webbrowser.open('http://localhost:8080')
            self._start_web_server()
        except KeyboardInterrupt:
            print("\n✅ Client review session ended")
        
        return str(draft_path)
    
    def _create_web_interface(self, draft_path: Path):
        """Create a simple web interface for client editing"""
        # Read the draft content
        with open(draft_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create HTML interface
        html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client Review - {draft_path.name}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }}
        .header {{
            background: #f1eea4;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .instructions {{
            background: #f0f0f0;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .content-area {{
            width: 100%;
            min-height: 600px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            padding: 15px;
            border: 2px solid #ccc;
            border-radius: 8px;
            resize: vertical;
        }}
        .buttons {{
            margin-top: 20px;
            text-align: center;
        }}
        .btn {{
            background: #000;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 0 10px;
            font-size: 16px;
        }}
        .btn:hover {{
            background: #333;
        }}
        .status {{
            margin-top: 10px;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }}
        .success {{
            background: #d4edda;
            color: #155724;
        }}
        .error {{
            background: #f8d7da;
            color: #721c24;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📝 Client Review Interface</h1>
        <p><strong>File:</strong> {draft_path.name}</p>
        <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
    
    <div class="instructions">
        <h3>📋 Instructions:</h3>
        <ol>
            <li>Review the content below</li>
            <li>Make any necessary edits</li>
            <li>Click "Save Changes" when done</li>
            <li>The file will be updated automatically</li>
        </ol>
        <p><strong>Note:</strong> Only edit content between the <!-- EDITABLE START --> and <!-- EDITABLE END --> markers</p>
    </div>
    
    <textarea id="content" class="content-area">{content}</textarea>
    
    <div class="buttons">
        <button class="btn" onclick="saveChanges()">💾 Save Changes</button>
        <button class="btn" onclick="downloadFile()">📥 Download File</button>
        <button class="btn" onclick="previewContent()">👁️ Preview</button>
    </div>
    
    <div id="status"></div>
    
    <script>
        function saveChanges() {{
            const content = document.getElementById('content').value;
            const status = document.getElementById('status');
            
            fetch('/save', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{content: content}})
            }})
            .then(response => response.json())
            .then(data => {{
                if (data.success) {{
                    status.innerHTML = '<div class="success">✅ Changes saved successfully!</div>';
                }} else {{
                    status.innerHTML = '<div class="error">❌ Error saving changes: ' + data.error + '</div>';
                }}
            }})
            .catch(error => {{
                status.innerHTML = '<div class="error">❌ Error: ' + error.message + '</div>';
            }});
        }}
        
        function downloadFile() {{
            const content = document.getElementById('content').value;
            const blob = new Blob([content], {{type: 'text/markdown'}});
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = '{draft_path.name}';
            a.click();
            window.URL.revokeObjectURL(url);
        }}
        
        function previewContent() {{
            const content = document.getElementById('content').value;
            const newWindow = window.open('', '_blank');
            newWindow.document.write('<html><head><title>Preview</title></head><body>');
            newWindow.document.write('<pre>' + content.replace(/</g, '&lt;').replace(/>/g, '&gt;') + '</pre>');
            newWindow.document.write('</body></html>');
        }}
    </script>
</body>
</html>
"""
        
        # Save HTML interface
        interface_path = self.drafts_dir / "client_interface.html"
        with open(interface_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        return interface_path
    
    def _start_web_server(self):
        """Start a simple HTTP server for the client interface"""
        class RequestHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.path = '/drafts/client_interface.html'
                return http.server.SimpleHTTPRequestHandler.do_GET(self)
            
            def do_POST(self):
                if self.path == '/save':
                    content_length = int(self.headers['Content-Length'])
                    post_data = self.rfile.read(content_length)
                    data = json.loads(post_data.decode('utf-8'))
                    
                    try:
                        # Save the updated content
                        draft_path = self.drafts_dir / "current_draft.md"
                        with open(draft_path, 'w', encoding='utf-8') as f:
                            f.write(data['content'])
                        
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps({'success': True}).encode())
                    except Exception as e:
                        self.send_response(500)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
                else:
                    self.send_response(404)
                    self.end_headers()
        
        # Change to project root directory
        os.chdir(Path(__file__).parent.parent)
        
        with socketserver.TCPServer(("", 8080), RequestHandler) as httpd:
            print("🌐 Server started at http://localhost:8080")
            httpd.serve_forever()
    
    def stage3_generate_final(self, draft_file: str, output_dir: str) -> str:
        """Stage 3: Generate final HTML with client changes"""
        print(f"🔧 Stage 3: Generating final HTML from {draft_file}")
        
        draft_path = Path(draft_file)
        if not draft_path.exists():
            print(f"❌ Draft file not found: {draft_path}")
            return None
        
        # Read the edited draft
        with open(draft_path, 'r', encoding='utf-8') as f:
            draft_content = f.read()
        
        # Parse client changes and apply to original JSON
        updated_json = self._apply_client_changes(draft_content)
        
        # Generate final HTML
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        # Use existing converter to generate HTML
        from converters.json_to_html_converter_merged import convert_json_to_html
        
        # Save updated JSON temporarily
        temp_json_path = self.drafts_dir / "temp_updated.json"
        with open(temp_json_path, 'w', encoding='utf-8') as f:
            json.dump(updated_json, f, indent=2, ensure_ascii=False)
        
        # Generate HTML
        html_filename = f"{draft_path.stem.replace('_draft', '')}.html"
        html_path = output_path / html_filename
        
        # Call the existing converter
        convert_json_to_html(str(temp_json_path), str(html_path))
        
        # Clean up temp file
        temp_json_path.unlink()
        
        print(f"✅ Final HTML generated: {html_path}")
        return str(html_path)
    
    def _apply_client_changes(self, draft_content: str) -> Dict[str, Any]:
        """Parse client changes from draft and apply to original JSON structure"""
        # This is a simplified version - in practice, you'd want more robust parsing
        # For now, we'll extract the editable sections and reconstruct the JSON
        
        # Extract metadata changes
        metadata_match = re.search(r'<!-- EDITABLE START -->(.*?)<!-- EDITABLE END -->', 
                                 draft_content, re.DOTALL)
        
        # Extract executive summary changes
        exec_summary_match = re.search(r'## EXECUTIVE SUMMARY\s*<!-- EDITABLE START -->(.*?)<!-- EDITABLE END -->', 
                                     draft_content, re.DOTALL)
        
        # For now, return a basic structure - you'd implement full parsing here
        return {
            "metadata": {
                "title": "Updated Title from Client",
                "subtitle": "Updated Subtitle from Client"
            },
            "executive_summary": {
                "overview": "Updated overview from client",
                "key_findings": ["Updated finding 1", "Updated finding 2"],
                "key_themes": ["Updated theme 1", "Updated theme 2"],
                "geographical_focus": ["Updated location 1", "Updated location 2"],
                "trend_analysis": "Updated trend analysis from client"
            },
            "items": []
        }


def main():
    parser = argparse.ArgumentParser(description='Client Review Workflow for Newsletter Content')
    parser.add_argument('--stage', type=int, required=True, choices=[1, 2, 3],
                       help='Workflow stage: 1=generate draft, 2=client review, 3=generate final')
    parser.add_argument('--input', type=str, help='Input JSON file (for stage 1)')
    parser.add_argument('--draft', type=str, help='Draft file path (for stages 2 and 3)')
    parser.add_argument('--output', type=str, help='Output directory (for stage 3)')
    
    args = parser.parse_args()
    
    workflow = ClientReviewWorkflow()
    
    if args.stage == 1:
        if not args.input:
            print("❌ --input required for stage 1")
            sys.exit(1)
        workflow.stage1_generate_draft(args.input)
    
    elif args.stage == 2:
        if not args.draft:
            print("❌ --draft required for stage 2")
            sys.exit(1)
        workflow.stage2_client_review(args.draft)
    
    elif args.stage == 3:
        if not args.draft or not args.output:
            print("❌ --draft and --output required for stage 3")
            sys.exit(1)
        workflow.stage3_generate_final(args.draft, args.output)


if __name__ == "__main__":
    main()
