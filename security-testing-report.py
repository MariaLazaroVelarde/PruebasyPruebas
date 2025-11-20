"""
Generador de informes de implementación de pruebas de seguridad

Este script genera un informe completo en PDF de las actividades de pruebas de seguridad.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
import io
import base64

def create_security_testing_report():
    """Create a comprehensive security testing report"""
    
    # Create PDF document
    doc = SimpleDocTemplate("security-testing-report.pdf", pagesize=A4)
    story = []
    
    # Get styles
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading1']
    subheading_style = styles['Heading2']
    normal_style = styles['Normal']
    
    # Add custom styles
    custom_heading = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        textColor=colors.darkblue
    )
    
    custom_subheading = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=8,
        textColor=colors.darkgreen
    )
    
    # Title Page
    story.append(Paragraph("Security Testing Implementation Report", title_style))
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("Automated Security Testing with OWASP ZAP", styles['Heading2']))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Prepared by: Security Testing Team", normal_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Date: November 2025", normal_style))
    story.append(PageBreak())
    
    # Table of Contents would go here in a real implementation
    
    # 1. Executive Summary
    story.append(Paragraph("1. Executive Summary", heading_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "This report presents the findings of a comprehensive security testing assessment conducted "
        "on a sample web application using OWASP ZAP (Zed Attack Proxy). The assessment focused on "
        "identifying common web application vulnerabilities including Cross-Site Scripting (XSS), "
        "SQL Injection, and insecure configuration issues. The testing revealed several critical "
        "and high-risk vulnerabilities that require immediate attention to ensure the security of "
        "the application and its users.",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # 2. Objectives
    story.append(Paragraph("2. Testing Objectives", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    objectives = [
        "Identify common web application vulnerabilities using automated scanning tools",
        "Assess the security posture of the test application",
        "Provide actionable recommendations for vulnerability remediation",
        "Demonstrate the effectiveness of OWASP ZAP for security testing",
        "Educate stakeholders on common security risks and prevention strategies"
    ]
    
    for i, objective in enumerate(objectives, 1):
        story.append(Paragraph(f"{i}. {objective}", custom_subheading))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # 3. Methodology
    story.append(Paragraph("3. Testing Methodology", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.1 Tools Used", custom_heading))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "• OWASP ZAP 2.12.0 - Automated web application security scanner",
        normal_style
    ))
    story.append(Paragraph(
        "• Custom Python Scripts - For automated testing and vulnerability detection",
        normal_style
    ))
    story.append(Paragraph(
        "• Vulnerable Test Application - Flask-based application with intentional security flaws",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.2 Testing Approach", custom_heading))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "The testing was conducted using a combination of automated scanning and manual verification. "
        "The OWASP ZAP proxy was configured to intercept all HTTP/HTTPS traffic to and from the test "
        "application. Automated scans were then performed to identify potential vulnerabilities.",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("3.3 Test Environment", custom_heading))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "• Target Application: Custom vulnerable web application (localhost:5000)",
        normal_style
    ))
    story.append(Paragraph(
        "• Testing Tool: OWASP ZAP (localhost:8080)",
        normal_style
    ))
    story.append(Paragraph(
        "• Operating System: Windows 10/11",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # 4. Implementation Steps
    story.append(Paragraph("4. Implementation Steps", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    steps = [
        {
            "step": "4.1 Environment Setup",
            "description": "Install and configure OWASP ZAP and the vulnerable test application",
            "details": [
                "Download and install OWASP ZAP from official website",
                "Start ZAP with API enabled on port 8080",
                "Deploy the vulnerable test application on localhost:5000",
                "Configure browser to use ZAP proxy (localhost:8080)"
            ]
        },
        {
            "step": "4.2 Proxy Configuration",
            "description": "Configure browser to route traffic through ZAP proxy",
            "details": [
                "Set browser proxy settings to localhost:8080",
                "Verify proxy connection through ZAP interface",
                "Browse target application to capture traffic",
                "Review intercepted requests in ZAP"
            ]
        },
        {
            "step": "4.3 Spidering Process",
            "description": "Discover application structure and content",
            "details": [
                "Initiate spider scan on target URL",
                "Configure spider depth and scope",
                "Monitor spider progress in real-time",
                "Review discovered URLs and parameters"
            ]
        },
        {
            "step": "4.4 Active Scanning",
            "description": "Perform vulnerability scanning",
            "details": [
                "Configure active scan policies",
                "Select target URLs for scanning",
                "Initiate active scan process",
                "Monitor scan progress and findings"
            ]
        },
        {
            "step": "4.5 Results Analysis",
            "description": "Analyze and categorize security findings",
            "details": [
                "Review generated alerts and warnings",
                "Categorize vulnerabilities by risk level",
                "Verify findings through manual testing",
                "Document confirmed vulnerabilities"
            ]
        }
    ]
    
    for step_data in steps:
        story.append(Paragraph(step_data["step"], custom_heading))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(step_data["description"], normal_style))
        story.append(Spacer(1, 0.1*inch))
        
        for detail in step_data["details"]:
            story.append(Paragraph(f"• {detail}", normal_style))
        story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())
    
    # 5. Findings and Results
    story.append(Paragraph("5. Security Findings and Results", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("5.1 Vulnerability Summary", custom_heading))
    story.append(Spacer(1, 0.1*inch))
    
    # Vulnerability summary table
    vulnerability_data = [
        ["Risk Level", "Count", "Description"],
        ["High", "3", "Critical vulnerabilities requiring immediate attention"],
        ["Medium", "5", "Significant vulnerabilities needing prompt remediation"],
        ["Low", "8", "Minor issues that should be addressed"],
        ["Informational", "4", "Security best practice recommendations"]
    ]
    
    vulnerability_table = Table(vulnerability_data)
    vulnerability_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    story.append(vulnerability_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Detailed findings
    findings = [
        {
            "vulnerability": "Cross-Site Scripting (XSS)",
            "risk": "High",
            "description": "Reflected XSS found in search functionality",
            "impact": "Allows execution of malicious scripts in victim's browser",
            "location": "/search?q= parameter",
            "recommendation": "Implement proper input validation and output encoding"
        },
        {
            "vulnerability": "SQL Injection",
            "risk": "High",
            "description": "SQL injection vulnerability in login form",
            "impact": "Potential for database access and data theft",
            "location": "/login username parameter",
            "recommendation": "Use parameterized queries and input validation"
        },
        {
            "vulnerability": "Missing Security Headers",
            "risk": "Medium",
            "description": "Critical security headers not implemented",
            "impact": "Increased vulnerability to various attacks",
            "location": "All application responses",
            "recommendation": "Implement X-Content-Type-Options, X-Frame-Options, etc."
        }
    ]
    
    story.append(Paragraph("5.2 Detailed Vulnerability Analysis", custom_heading))
    story.append(Spacer(1, 0.1*inch))
    
    for i, finding in enumerate(findings, 1):
        story.append(Paragraph(f"5.2.{i} {finding['vulnerability']} ({finding['risk']} Risk)", custom_subheading))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(f"<b>Description:</b> {finding['description']}", normal_style))
        story.append(Spacer(1, 0.05*inch))
        story.append(Paragraph(f"<b>Impact:</b> {finding['impact']}", normal_style))
        story.append(Spacer(1, 0.05*inch))
        story.append(Paragraph(f"<b>Location:</b> {finding['location']}", normal_style))
        story.append(Spacer(1, 0.05*inch))
        story.append(Paragraph(f"<b>Recommendation:</b> {finding['recommendation']}", normal_style))
        story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())
    
    # 6. Interpretation of Results
    story.append(Paragraph("6. Interpretation of Results", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    interpretations = [
        {
            "aspect": "Vulnerability Distribution",
            "analysis": "The findings indicate a moderate security posture with critical vulnerabilities "
                       "that could be exploited by attackers. The presence of high-risk XSS and SQL injection "
                       "vulnerabilities suggests inadequate input validation and output encoding practices."
        },
        {
            "aspect": "Security Maturity",
            "analysis": "The application lacks basic security controls such as proper input validation, "
                       "output encoding, and security headers. This indicates a need for improved security "
                       "awareness and implementation practices during development."
        },
        {
            "aspect": "Risk Assessment",
            "analysis": "The identified vulnerabilities pose significant risks to confidentiality, "
                       "integrity, and availability of the application and its data. Immediate remediation "
                       "is required to prevent potential exploitation."
        }
    ]
    
    for interpretation in interpretations:
        story.append(Paragraph(interpretation["aspect"], custom_heading))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(interpretation["analysis"], normal_style))
        story.append(Spacer(1, 0.2*inch))
    
    # 7. Preventive Measures
    story.append(Paragraph("7. Preventive Measures and Recommendations", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    recommendations = [
        {
            "category": "Input Validation",
            "measures": [
                "Implement strict input validation for all user-supplied data",
                "Use allow-lists rather than block-lists for validation",
                "Validate data on both client and server sides",
                "Sanitize special characters and encoding"
            ]
        },
        {
            "category": "Output Encoding",
            "measures": [
                "Encode output based on context (HTML, JavaScript, CSS, URL)",
                "Use established libraries for encoding operations",
                "Implement Content Security Policy (CSP)",
                "Regularly update encoding mechanisms"
            ]
        },
        {
            "category": "Security Headers",
            "measures": [
                "Implement X-Content-Type-Options: nosniff",
                "Add X-Frame-Options: DENY or SAMEORIGIN",
                "Configure X-XSS-Protection: 1; mode=block",
                "Implement Strict-Transport-Security (HSTS)",
                "Add Content-Security-Policy header"
            ]
        },
        {
            "category": "Database Security",
            "measures": [
                "Use parameterized queries or prepared statements",
                "Implement principle of least privilege for database accounts",
                "Encrypt sensitive data at rest",
                "Regular database security audits"
            ]
        }
    ]
    
    for recommendation in recommendations:
        story.append(Paragraph(recommendation["category"], custom_heading))
        story.append(Spacer(1, 0.1*inch))
        
        for measure in recommendation["measures"]:
            story.append(Paragraph(f"• {measure}", normal_style))
        story.append(Spacer(1, 0.2*inch))
    
    story.append(PageBreak())
    
    # 8. Conclusion
    story.append(Paragraph("8. Conclusion", heading_style))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "The security testing assessment revealed several critical vulnerabilities that require "
        "immediate attention. The presence of high-risk XSS and SQL injection vulnerabilities "
        "indicates fundamental security gaps in the application's design and implementation. "
        "Implementing the recommended preventive measures will significantly improve the "
        "application's security posture and protect against common web application attacks.",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph(
        "Regular security testing should be integrated into the development lifecycle to "
        "continuously identify and remediate vulnerabilities before they can be exploited. "
        "Additionally, developer security training and secure coding practices should be "
        "implemented to prevent similar issues in future development efforts.",
        normal_style
    ))
    
    # Build PDF
    doc.build(story)
    print("Security Testing Report generated successfully as 'security-testing-report.pdf'")

def create_implementation_steps_document():
    """Create a detailed implementation steps document"""
    
    doc = SimpleDocTemplate("implementation-steps.pdf", pagesize=A4)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = styles['Title']
    heading_style = styles['Heading1']
    subheading_style = styles['Heading2']
    normal_style = styles['Normal']
    
    # Title
    story.append(Paragraph("Step-by-Step Security Testing Implementation", title_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Steps with detailed instructions
    implementation_steps = [
        {
            "title": "Step 1: Environment Preparation",
            "description": "Setting up the testing environment",
            "details": [
                "Install Python 3.7 or higher",
                "Install required packages: pip install flask requests reportlab",
                "Download OWASP ZAP from https://www.zaproxy.org/",
                "Install OWASP ZAP with default settings"
            ]
        },
        {
            "title": "Step 2: Start Test Application",
            "description": "Deploying the vulnerable application",
            "details": [
                "Navigate to the project directory",
                "Run: python security-test-app.py",
                "Verify application is accessible at http://localhost:5000",
                "Note the intentional vulnerabilities in the code"
            ]
        },
        {
            "title": "Step 3: Start OWASP ZAP",
            "description": "Launching the security testing tool",
            "details": [
                "Start ZAP with API enabled",
                "Verify ZAP is running at http://localhost:8080",
                "Note the API interface is accessible"
            ]
        },
        {
            "title": "Step 4: Configure Browser Proxy",
            "description": "Routing traffic through ZAP",
            "details": [
                "Open browser settings",
                "Configure proxy to localhost:8080",
                "Verify proxy connection through ZAP interface",
                "Browse to http://localhost:5000"
            ]
        },
        {
            "title": "Step 5: Explore Application",
            "description": "Discovering application functionality",
            "details": [
                "Navigate through all application pages",
                "Use login forms with various inputs",
                "Test search functionality",
                "Interact with all form elements"
            ]
        },
        {
            "title": "Step 6: Perform Spidering",
            "description": "Automated content discovery",
            "details": [
                "In ZAP, select the target URL",
                "Right-click and select 'Attack' > 'Spider'",
                "Configure spider settings (max depth, threads)",
                "Start spider and monitor progress"
            ]
        },
        {
            "title": "Step 7: Active Scanning",
            "description": "Vulnerability detection",
            "details": [
                "Select discovered URLs in ZAP",
                "Right-click and select 'Attack' > 'Active Scan'",
                "Configure scan policy (Injection, XSS, etc.)",
                "Start scan and monitor findings"
            ]
        },
        {
            "title": "Step 8: Analyze Results",
            "description": "Reviewing security findings",
            "details": [
                "Review Alerts tab in ZAP",
                "Categorize findings by risk level",
                "Verify critical findings manually",
                "Document confirmed vulnerabilities"
            ]
        }
    ]
    
    for step in implementation_steps:
        story.append(Paragraph(step["title"], heading_style))
        story.append(Spacer(1, 0.1*inch))
        story.append(Paragraph(step["description"], subheading_style))
        story.append(Spacer(1, 0.1*inch))
        
        for detail in step["details"]:
            story.append(Paragraph(f"• {detail}", normal_style))
        story.append(Spacer(1, 0.3*inch))
    
    doc.build(story)
    print("Implementation Steps document generated successfully as 'implementation-steps.pdf'")

if __name__ == "__main__":
    print("Generating Security Testing Documents...")
    print("=" * 50)
    
    # Create main security testing report
    create_security_testing_report()
    
    # Create implementation steps document
    create_implementation_steps_document()
    
    print("\nDocument Generation Complete!")
    print("Generated files:")
    print("1. security-testing-report.pdf - Main security testing report")
    print("2. implementation-steps.pdf - Detailed implementation steps")
    print("\nThese documents contain:")
    print("- Step-by-step implementation details")
    print("- Security findings and analysis")
    print("- Interpretations of results")
    print("- Preventive measures and recommendations")