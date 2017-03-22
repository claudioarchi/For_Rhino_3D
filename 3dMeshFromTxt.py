#  Provides a scripting component for Grasshopper
#  Inputs:
#  textIds: The script variable must be a list Acces and ghdoc Object type hint
# refresh: The script variable must be an Item Acces and ghdoc Object type hint
#  Output:
#  pts: The a output variable (3d points in this case)

import scriptcontext as sc
import Rhino

__author__ = "cnunez"

pts = []
sc.doc = Rhino.RhinoDoc.ActiveDoc
for id in textIds:
    textObj = sc.doc.Objects.Find(id)
    textEntity = textObj.Geometry
    text = textEntity.Text
    pt = textEntity.Plane.Origin
    try:
        ptZ = float(text)
    except:
        textReplaced = text.replace(" ", ".")
        if textReplaced.endswith("."):
            textReplaced = textReplaced[:-1]
        ptZ = float(textReplaced)
    ptLifted = Rhino.Geometry.Point3d(pt.X, pt.Y, ptZ)
    pts.append(ptLifted)
sc.doc = ghdoc
