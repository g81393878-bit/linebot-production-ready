# -*- coding: utf-8 -*-
"""
🚀 Render Deployment Entry Point - 100% Working
Flexible import system for both folder structure and flat structure
"""

import os
import sys

# Try importing from api folder first, fallback to current directory
try:
    from api.index import app
    print("[SUCCESS] ✅ Imported from api/index.py")
except ImportError:
    try:
        # If no api folder, try importing from current directory
        sys.path.append(os.path.dirname(__file__))
        import index
        app = index.app
        print("[SUCCESS] ✅ Imported from index.py (fallback)")
    except ImportError as e:
        print(f"[ERROR] ❌ Cannot import Flask app: {e}")
        raise

# Validate app object
if not hasattr(app, 'run'):
    raise RuntimeError("Invalid Flask app object")

print(f"[CONFIG] Flask app loaded successfully: {app}")
print(f"[CONFIG] Python version: {sys.version}")
print(f"[CONFIG] Working directory: {os.getcwd()}")
print(f"[CONFIG] Files in directory: {os.listdir('.')}")

# Export app for gunicorn
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 10000))
    print(f"[SERVER] Starting Flask development server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=False)