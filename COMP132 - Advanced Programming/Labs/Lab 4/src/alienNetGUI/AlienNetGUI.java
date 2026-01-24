package alienNetGUI;

import aliennet.AlienNet;
import alien.Alien;

import java.awt.EventQueue;
import java.awt.Font;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.*;
import javax.swing.border.EmptyBorder;

public class AlienNetGUI extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private JTextField alienName;
	private JTextField msgInput;
	private JComboBox<String> alienType;
	private JComboBox<Alien> selectAlien;
	private JTextArea showMsg;

	private AlienNet alienNet = new AlienNet();

	public AlienNetGUI() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 500);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		JLabel lblNewLabel = new JLabel("Alien Name:");
		lblNewLabel.setBounds(6, 11, 120, 16);
		contentPane.add(lblNewLabel);

		alienName = new JTextField();
		alienName.setBounds(227, 6, 217, 26);
		contentPane.add(alienName);
		alienName.setColumns(10);

		alienType = new JComboBox<>(new String[] {"Common", "Elite", "Royal"});
		alienType.setBounds(227, 44, 217, 27);
		contentPane.add(alienType);

		JLabel lblNewLabel_1 = new JLabel("Type");
		lblNewLabel_1.setBounds(6, 48, 61, 16);
		contentPane.add(lblNewLabel_1);

		JButton btnRegAlien = new JButton("Register Alien");
		btnRegAlien.setBounds(227, 83, 217, 29);
		contentPane.add(btnRegAlien);

		JLabel lblNewLabel_2 = new JLabel("Select Alien");
		lblNewLabel_2.setBounds(6, 124, 120, 16);
		contentPane.add(lblNewLabel_2);

		selectAlien = new JComboBox<>();
		selectAlien.setBounds(6, 152, 438, 27);
		contentPane.add(selectAlien);

		msgInput = new JTextField();
		msgInput.setBounds(6, 191, 438, 47);
		contentPane.add(msgInput);
		msgInput.setColumns(10);

		JButton btnTrans = new JButton("Send Transmission");
		btnTrans.setFont(new Font("Dialog", Font.ITALIC, 12));
		btnTrans.setBounds(6, 250, 438, 29);
		contentPane.add(btnTrans);

		JScrollPane scrollPane = new JScrollPane();
		scrollPane.setBounds(6, 289, 438, 136);
		contentPane.add(scrollPane);

		showMsg = new JTextArea();
		showMsg.setEditable(false);
		scrollPane.setViewportView(showMsg);

		JButton btnExit = new JButton("Exit");
		btnExit.setFont(new Font("Dialog", Font.BOLD, 12));
		btnExit.setName("exitCloseButton");
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnExit.setBounds(327, 437, 117, 29);
		contentPane.add(btnExit);

		btnRegAlien.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String name = alienName.getText().trim();
				String type = (String) alienType.getSelectedItem();
				Alien newAlien = alienNet.addAlien(name, type);
				selectAlien.addItem(newAlien);
				JOptionPane.showMessageDialog(null, "Alien registered: " + newAlien.getName());
				alienName.setText("");
			}
		});

		btnTrans.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				Alien selected = (Alien) selectAlien.getSelectedItem();
				String msg = msgInput.getText().trim();
				selected.sendTransmission(msg);
				showMsg.append(selected.getName() + ": " + msg + "\n");
				msgInput.setText("");
			}
		});
		
		setVisible(true);
		setLocationRelativeTo(null);
	}
}