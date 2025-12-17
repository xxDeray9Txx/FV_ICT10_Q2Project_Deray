from pyscript import document
        from html import escape

        def set_contact():
            # Corrected the f-string logic to display text clearly
            name = "OBMC Fairview"
            address = "Napoli Street, Neapolitan IV, Quezon City"
            html = f"<strong>{escape(name)}</strong><br>{escape(address)}"
            document.getElementById("contact").innerHTML = html

        def add_announcement(e):
            txt_el = document.getElementById("ann_text")
            if not txt_el:
                return
            txt = txt_el.value
            if not txt or not txt.strip():
                return
            
            # Create the list item using Python
            li = document.createElement("li")
            li.textContent = txt.strip()
            document.getElementById("ann_list").appendChild(li)
            
            # Clear input after adding
            txt_el.value = ""

        def init_announcements():
            examples = ["Orientation — Aug 1", "Open House — Sep 10"]
            for ex in examples:
                li = document.createElement("li")
                li.textContent = ex
                document.getElementById("ann_list").appendChild(li)

        # Initialize content on load
        set_contact()
        init_announcements()